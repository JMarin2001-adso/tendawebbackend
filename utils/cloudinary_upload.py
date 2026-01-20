import cloudinary.uploader

def subir_imagen_cloudinary(file):
    try:
        result = cloudinary.uploader.upload(
            file,
            folder="productos"
        )
        return result["secure_url"]
    except Exception as e:
        raise Exception(f"Error subiendo imagen a Cloudinary: {str(e)}")
