import boto3
import sagemaker
from sagemaker.sklearn import SKLearn

def criar_sagemaker_cliente():
    session = sagemaker.Session()
    return session

def implantar_modelo_sagemaker(session, role, bucket, script_path, instance_type='ml.m4.xlarge'):
    sklearn_estimator = SKLearn(
        entry_point=script_path,
        role=role,
        instance_type=instance_type,
        framework_version='0.23-1',
        py_version='py3',
        sagemaker_session=session
    )
    return sklearn_estimator
