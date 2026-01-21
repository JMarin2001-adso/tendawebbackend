import cloudinary.uploader

def subir_imagen_cloudinary(file):
    try:
        resultado = cloudinary.uploader.upload(
            file,
            folder="productos"
        )
        return resultado["secure_url"]
    except Exception as e:
        raise Exception(f"Error subiendo imagen a Cloudinary: {str(e)}")

