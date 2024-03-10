import bcrypt

class PasswordHandler:
    def hash_pass(password: str) -> str:
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(password.encode(), salt)
        return password
    
    def verify_passowrd(hashed_pass: str, raw_pass: str):
        return bcrypt.checkpw(raw_pass.encode(), hashed_pass.encode())
