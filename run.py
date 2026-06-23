from app import app, db

if __name__ == "__main__":
    # Crea las tablas de tu taller y las de autenticación automáticamente
    with app.app_context():
        db.create_all()
    
    # Arranca el servidor local en modo desarrollo
    app.run(host="0.0.0.0", port=8080, debug=True)