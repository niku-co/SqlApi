import os

class Config:
    DATABASES = {
        "db1": {
            "SERVER": os.getenv("DB1_SERVER", "c901884d-10d0-4b98-b5d0-e0d930fd85ad.hsvc.ir"),
            "PORT": os.getenv("DB1_PORT", "1433"),
            "DATABASE": os.getenv("DB1_DATABASE", "DBtest"),
            "USER": os.getenv("DB1_USER", "sa"),
            "PASSWORD": os.getenv("DB1_PASSWORD", "3zVeYopmN2uUe6aqAyGoXKwZFEa1SjAD"),
        },
        "db2": {
            "SERVER": os.getenv("DB2_SERVER", "c901884d-10d0-4b98-b5d0-e0d930fd85ad.hsvc.ir"),
            "PORT": os.getenv("DB2_PORT", "1433"),
            "DATABASE": os.getenv("DB2_DATABASE", "db1402"),
            "USER": os.getenv("DB2_USER", "sa"),
            "PASSWORD": os.getenv("DB2_PASSWORD", "3zVeYopmN2uUe6aqAyGoXKwZFEa1SjAD"),
        },
    }
