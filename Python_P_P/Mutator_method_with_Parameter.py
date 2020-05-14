# Instance Method - Mutator Method / setter Method

class Mobile:
        def set_model(self,m):      #Mutator Method
            self.model=m

realme=Mobile()
realme.set_model("Realme x")  # calling Mutator method
print(realme.model)
