import Protos.product_pb2_grpc as pb2_grpc
import Protos.product_pb2 as pb2

products = []


class ProductService(pb2_grpc.ProductService):
    def __init__(self, *args, **kwargs):
        pass

    def AddProduct(self, request, context):
        id = len(products) + 1
        products.append(
            {
                "id": id,
                "name": request.name,
                "valor": request.valor,
            }
        )
        return pb2.ProductResponse(
            id=id, name=request.name, valor=request.valor, msg="add ok"
        )

    def GetProduct(self, request, context):
        # busca na lista
        product = next((p for p in products if p["id"] == int(request.id)), None)
        if product:
            return pb2.ProductResponse(
                id=product["id"],
                name=product["name"],
                valor=product["valor"],
                msg="get ok",
            )
        else:
            return pb2.ProductResponse(id=0, name="", valor="", msg="get erro")

    def UpdateProduct(self, request, context):
        # busca na lista
        product = next((p for p in products if p["id"] == int(request.id)), None)
        if product:
            # atualiza os dados
            product["name"] = request.name
            product["valor"] = request.valor
            return pb2.ProductResponse(
                id=product["id"],
                name=product["name"],
                valor=product["valor"],
                msg="update ok",
            )
        else:
            return pb2.ProductResponse(id=0, name="", valor="", msg="update erro")

    def DeleteProduct(self, request, context):
        # busca na lista
        product = next((p for p in products if p["id"] == int(request.id)), None)
        if product:
            # exclui o produto
            products.remove(product)
            return pb2.ProductResponse(
                id=product["id"],
                name=product["name"],
                valor=product["valor"],
                msg="del ok",
            )
        else:
            return pb2.ProductResponse(id=0, name="", valor="", msg="del erro")
