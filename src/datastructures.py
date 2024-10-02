
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
                "id": self._generateId(),
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }]  # Lista inicial de miembros vacía

    # Método para generar un ID aleatorio para los miembros
    def _generateId(self):
        return randint(0, 99999999)

    # Método para agregar un nuevo miembro a la familia
    def add_member(self, member):
        # Si el miembro no tiene 'id', generamos uno
        if "id" not in member:
            member["id"] = self._generateId()
        
        # Agregamos el nuevo miembro a la lista de miembros
        self._members.append(member)
        return member

    # Método para eliminar un miembro de la lista de miembros
    def delete_member(self, id):
        # Filtramos la lista de miembros para eliminar el miembro con el id proporcionado
        self._members = [member for member in self._members if member["id"] != id]
        return {"done": True}

    # Método para obtener un miembro por su id
    def get_member(self, id):
        # Buscamos el miembro en la lista que tiene el id proporcionado
        for member in self._members:
            if member["id"] == id:
                return member
        return None  # Si no se encuentra el miembro, retornamos None

    # Método para actualizar un miembro existente
    def update_member(self, id, updates):
        # Buscamos el miembro a actualizar
        for i, member in enumerate(self._members):
            if member["id"] == id:
                # Actualizamos los campos del miembro con los datos proporcionados en 'updates'
                self._members[i].update(updates)
                return self._members[i]
        return None  # Si no se encuentra el miembro, retornamos None

    # Este método ya está hecho, retorna todos los miembros de la familia
    def get_all_members(self):
        return self._members