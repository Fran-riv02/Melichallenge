import logging
import boto3
from botocore.exceptions import ClientError


def upload_file():
    
    s3_client = boto3.client('s3')

    action=input("¿Si/No?")

    while(action=="Si"):

        bucket_name = input("Ingrese el nombre del bucket en S3: ")
        object_name = input("Ingrese el archivo: ") 
        file_name = input("Ingrese el nombre que tendra el archivo en S3: ")

        try:
            s3_client.upload_file(object_name, bucket_name, file_name)
            print("Archivo subido correctamente")
            
        except ClientError as e:
            logging.error(e)
            print("No se puede ejecutar correctamente el comando")

        else:
            print("Proceso finalizado")

        action=input("¿Desea subir otro archivo? S/N: ")

def dowload_file():

    s3_client = boto3.client('s3')

    action=input("¿Si/No?")

    while(action=="Si"):

        bucket_name = input("Ingrese el nombre del bucket en S3: ")
        object_name = input("Ingrese el archivo a descargar: ") 
        file_name = input("Ingrese el nombre con el que quiere que se guarde el archivo: ")

        try:
            s3_client.dowload_file(object_name, bucket_name, file_name)
            print("Archivo descargado correctamente")
            
        except ClientError as e:
            logging.error(e)
            print("No se puede ejecutar correctamente el comando")

        else:
            print("Proceso finalizado")
    
        

print("¿Querés subir archivos a S3?")
upload_file()

print("¿Querés descargar archivos de S3?")
dowload_file()
        
