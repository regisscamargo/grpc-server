import grpc
from concurrent import futures
import Protos.user_pb2_grpc as user_pb2_grpc
import Protos.product_pb2_grpc as product_pb2_grpc
import Services.UserService as user_service
import Services.ProductService as product_service


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(user_service.UserService(), server)
    product_pb2_grpc.add_ProductServiceServicer_to_server(
        product_service.ProductService(), server
    )
    server.add_insecure_port("[::]:50051")
    print("Server started at 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
