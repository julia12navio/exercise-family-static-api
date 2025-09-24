"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        new_member = dict(member) if member else {}
        if "id" not in new_member or new_member["id"] is None:
            new_member["id"] = self._generate_id()
        new_member["last_name"] = self.last_name
        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        for idx, m in enumerate(self._members):
            if m.get("id") == id:
                self._members.pop(idx)
                return True
        return False

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        for m in self._members:
            if m.get("id") == id:
                return m
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members