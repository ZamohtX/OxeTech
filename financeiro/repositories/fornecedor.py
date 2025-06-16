from financeiro.models.fornecedor import Fornecedor

class FornecedorRepository:

    def get_all(self):
        return Fornecedor.objects.all()


    def get_by_id(self, pk: int):
        try:
            return Fornecedor.objects.get(id=pk)
        except Fornecedor.DoesNotExist:
            return None
        

    def create(self, data: dict) -> Fornecedor:
        return Fornecedor.objects.create(**data)
    
    def update(self, pk: int, data: dict) -> Fornecedor:
        fornecedor = self.get_by_id(pk)
        if fornecedor:
            for key, value in data.items():
                setattr(fornecedor, key, value)
            fornecedor.save()
            return fornecedor
        return None
    
    def delete(self, pk: int) -> bool:
        fornecedor = self.get_by_id(pk)
        if fornecedor:
            fornecedor.delete()
            return True
        return False
    























