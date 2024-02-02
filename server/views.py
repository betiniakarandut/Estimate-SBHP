from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_session import Session
from config import ApplicationConfig
from models import db, User
from physical_properties.conversions import evaluate_scrhs
from physical_properties.staticbhp import StaticBHP
from physical_properties.pseudoreduced_properties import pseudo_reduced_temp, pseudo_reduced_wellhead_pressure
from physical_properties.pseudocritical_properties import natural_gas_systems, natural_gas_systems2

app = Flask(__name__)
CORS(app)

app.config.from_object(ApplicationConfig)

bcrypt = Bcrypt(app)
# Session(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    # Check for existing user (using PostgreSQL-specific keyword 'EXISTS')
    user_exists = db.session.query(db.exists().where(User.email == email)).scalar()
    
    if user_exists:
        return "Error: User already exists", 409

    hashed_password = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')
    new_user = User(email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"id": new_user.id, "email": new_user.email})


@app.route("/api/login", methods=["POST", "GET"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"Error": "Unauthorized"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"Error": "Unauthorized"}), 401
    
    session["key"] = user.id

    return jsonify({"id": user.id, "email": user.email})

@app.route("/api/calculate_properties", methods=["POST", "GET"])
def calculate_properties_api():
    """POST inputs from the user
    
    Returns:
        Renders the result page and passes computed values of gas properties
    """

    try:
        # Get input values from the form
        data = request.get_json()
        well_depth = float(data.get("well_depth"))
        temp_avg_sys = float(data.get("temp_avg_sys"))
        gas_specific_gravity = float(data.get("gas_specific_gravity"))
        static_wellhead_pressure = float(data.get("static_wellhead_pressure"))

        # Calculate pseudocritical properties of the gas system
        tpc_natural_gas_systems = natural_gas_systems(gas_specific_gravity)
        ppc_natural_gas_systems = natural_gas_systems2(gas_specific_gravity)

        # Call functions from physical_properties/ with the input values
        scrhs = evaluate_scrhs(gas_specific_gravity, well_depth, temp_avg_sys)
        reduced_temp = pseudo_reduced_temp(temp_avg_sys, gas_specific_gravity)
        reduced_pressure = pseudo_reduced_wellhead_pressure(static_wellhead_pressure, gas_specific_gravity)

        # Creates an instance of the StaticBHP class
        sbhp = StaticBHP()

        static_bhp_result = sbhp.print_staticbhp(reduced_temp, reduced_pressure, scrhs, gas_specific_gravity)

        return jsonify(
            {
                "scrhs": scrhs,
                "reduced_temp": reduced_temp,
                "reduced_pressure": reduced_pressure,
                "tpc_natural_gas_systems": tpc_natural_gas_systems,
                "ppc_natural_gas_systems": ppc_natural_gas_systems,
                "static_wellhead_pressure": static_wellhead_pressure,
                "static_bhp_result": static_bhp_result
            }
        )
    except Exception as e:
        return jsonify({"error": f"Ensure that all input fields are satisfied and are within the given range - {e}"})


if __name__=="__main__":
    app.run(debug=True)