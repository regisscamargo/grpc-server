import Protos.user_pb2_grpc as pb2_grpc
import Protos.user_pb2 as pb2

usuarios = []


class UserService(pb2_grpc.UserService):
    def __init__(self, *args, **kwargs):
        pass

    def AddUser(self, request, context):
        id = len(usuarios) + 1
        usuarios.append(
            {
                "id": id,
                "name": request.name,
                "email": request.email,
                "idade": 12,
                "adress": "sc",
                "state": "sc",
            }
        )
        return pb2.UserResponse(
            id=id, name=request.name, email=request.email, msg="add ok"
        )

    def GetUser(self, request, context):
        # busca na lista
        user = next((c for c in usuarios if c["id"] == int(request.id)), None)
        if user:
            return pb2.UserResponse(
                id=user["id"], name=user["name"], email=user["email"], msg="get ok"
            )
        else:
            return pb2.UserResponse(id=0, name="", email="", msg="get erro")

    def UpdateUser(self, request, context):
        # busca na lista
        user = next((c for c in usuarios if c["id"] == int(request.id)), None)
        if user:
            # atualiza os dados
            user["name"] = request.name
            user["email"] = request.email
            return pb2.UserResponse(
                id=user["id"], name=user["name"], email=user["email"], msg="update ok"
            )
        else:
            return pb2.UserResponse(id=0, name="", email="", msg="update erro")

    def DeleteUser(self, request, context):
        # busca na lista
        user = next((c for c in usuarios if c["id"] == int(request.id)), None)
        if user:
            # exclui o usuário
            usuarios.remove(user)
            return pb2.UserResponse(
                id=user["id"], name=user["name"], email=user["email"], msg="del ok"
            )
        else:
            return pb2.UserResponse(id=0, name="", email="", msg="del erro")
