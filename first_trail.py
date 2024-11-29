# import mlflow

# def calculate_sum(x,y):
#     return x*y


# if __name__ == '__main__':
#     #starting the server of mlflow
#     with mlflow.start_run():
#         x,y=75,10
#         z=calculate_sum(x,y)
#         #tracking the experiment with the mlflow
#         mlflow.log_param("x",x)
#         mlflow.log_param("y",y)
#         mlflow.log_metric("z",z)
        
        
import mlflow

def calculate_sum(x, y):
    return x * y

if __name__ == "__main__":
    # Set the tracking URI and create an experiment
    mlflow.set_tracking_uri("file:///C:/Users/lalit/Desktop/python practice/MLFLOW_new/MLFlow-Demo/mlruns")
    # mlflow.set_experiment("First Experiment")

    # Start MLflow run
    with mlflow.start_run():
        x, y = 75, 10
        z = calculate_sum(x, y)
        mlflow.log_param("x", x)
        mlflow.log_param("y", y)
        mlflow.log_metric("z", z)
        