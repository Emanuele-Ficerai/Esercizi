class Person:

    def __init__(self, name: str, surname: str, ssn: str) -> None:
        self.name: str = name
        self.surname: str= surname
        self.ssn: str = ssn
        
    
    def get_ssn(self) -> str:
        """
        This function returns the snn value
        input: none 
        return. self_snn: str, the function returns the snn value
        """
        return self.ssn
    
    def set_ssn(self, ssn: str) -> None:
        """
        This function set the attribute ssn 
        input: ssn : str, the parameter contains the user's ssn 
        return: None
        """
        
        raise Exception("You can't modify the ssn!")

   
    def get_name(self) -> str:
        """
        This function return a person's name
        input: none 
        return. self._name: str, the function returns the person's name 
        """

        return self.name
    
    def set_name(self, name: str) -> str:
        """
        This function set the attribute name 
        input: name : str, the parameter contains the user's name 
        return: None
        """
        raise Exception("You can't modify the name!")

person_1: Person = Person(name= "Emanuele", surname= " Ficerai" , ssn= "FCRMNL")
print(person_1.get_name())
print(person_1.get_ssn())

person_1.set_ssn(ssn="GLSE")
print(person_1.set_ssn())