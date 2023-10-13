import time

# Villian class

class Villian: 
    def __init__(self,name,HP,energy):
        self.name = name
        self.HP = HP
        self.energy = energy

class Gadget:
    def __init__(self,name,cost,quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        
    def CheckQuantitySTR(self):
        if self.quantity > -1:
            return f"{self.quantity}"
        else:
            return f"Infinite"
        
    def UseGadget(self):
        if self.quantity == 0:
            print("Out of resources")
            
        else: # When the player uses a gadget it will decrement the resources
            self.quantity -= 1
            print(self.name,"is used")         

# The weapon and shield classes will inherit the gadget class and add their speciific attributes

class Weapon(Gadget):
    def __init__(self,name,cost,quantity,damage):    
        super().__init__(self,name,cost,quantity)
        self.damage = damage
        
    def DescribeWeapon(self):
        print(self.name,":")
        print("Quantity:",self.CheckQuantitySTR())
        print("Energy Cost:",self.cost)
        print("Damage:",self.damage)    
        print()        

class Shield(Gadget):
    def __init__(self,name,cost,quantity,percentage):
        super().__init__(self,name,cost,quantity) 
        self.percentage = percentage
         
    def DescribeShield(self):
        print(self.name,":")
        print("Quantity:",self.CheckQuantitySTR())
        print("Energy Cost:",self.cost)
        print("Damage Reduction:",self.percentage,"%")  
        print()  

# Unnecessary classes, but couldn't delete them on time
# I had an idea of inheriting the villian as well and shomehow equip all these weapons
# in an array for each villian

class GruWeapon(Weapon):
    def __init__(self, name, cost, quantity, damage):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.damage = damage

class VectorWeapon(Weapon):
    def __init__(self, name, cost, quantity, damage):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.damage = damage

class GruShield(Shield):
    def __init__(self, name, cost, quantity, percentage):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.percentage = percentage

class VectorShield(Shield):
    def __init__(self, name, cost, quantity, percentage):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.percentage = percentage                           

# END OF CLASSES

P1 = Villian("Gru",100,500)
P2 = Villian("Vector",100,500)

# Gru's gadgets

Freeze_Gun     = GruWeapon("Freeze Gun",50,-1,11)     #infinite
Electric_Prod  = GruWeapon("Electric Prod" ,88,5,18)
Mega_Magnet    = GruWeapon("Mega Magnet"   ,92,3,10)  #reduce 20% of next opponent attack
Kalman_Missile = GruWeapon("Kalman Missile",120,1,20) #can't avoid it

Energy_Projected_BarrierGun = GruShield("Energy-Projected BarrierGun",20,-1,40) #infinite
Selective_Permeability      = GruShield("Selective Permeability",50,2,90)

# Vector's gadgets

Laser_Blasters         = VectorWeapon("Laser Blasters",40,-1,8) #infinite
Plasma_Grenades        = VectorWeapon("Plasma Grenades",56,8,13)
Sonic_Resonance_Cannon = VectorWeapon("Sonic Resonance Cannon",100,3,22)

Energy_Net_Trap   = VectorShield("Energy Net Trap",15,-1,32) #infinite
Quantum_Deflector = VectorShield("Quantum Deflector",40,3,80)

# Variables

class CurrentWeapon:
    def __init__(self, damageto, costto):
        self.damageto = damageto
        self.costto = costto
        
class CurrentShield:
    def __init__(self, percentageto, costto):
        self.percentageto = percentageto
        self.costto = costto        
    
# These are the variables that will help applying the damage and cost

P1_Weapon = CurrentWeapon(0,0)
P2_Weapon = CurrentWeapon(0,0)
P1_Shield = CurrentShield(1,0)
P2_Shield = CurrentShield(1,0)

Flag = 0 # for a special weapon

# Functions: just to list most stats

def GruStats():
    print("Gru's Health:",P1.HP)
    print("Gru's Energy:",P1.energy)
    print()
    
def VectorStats():
    print("Vector's Health:",P2.HP)
    print("Vector's Energy:",P2.energy)
    print()    
    
    
def AllStats():
    GruStats()
    VectorStats()    


def ListGruWeapons():
    print("Gru's weapons:")
    print()
    Freeze_Gun.DescribeWeapon()
    Electric_Prod.DescribeWeapon()
    Mega_Magnet.DescribeWeapon()
    Kalman_Missile.DescribeWeapon()
    print()
    
def ListGruShields():
    print("Gru's shields:")
    print()
    Energy_Projected_BarrierGun.DescribeShield()
    Selective_Permeability.DescribeShield()
    print()
    
def ListVectorWeapons():
    print("Vector's weapons:")
    print()
    Laser_Blasters.DescribeWeapon()
    Plasma_Grenades.DescribeWeapon()
    Sonic_Resonance_Cannon.DescribeWeapon()
    print()    
    
def ListVectorShields(): 
    print("Vector's shields:")
    print()
    Energy_Net_Trap.DescribeShield()
    Quantum_Deflector.DescribeShield()
    print()

    
def ListGruGadgets():
    ListGruWeapons()    
    ListGruShields()
        
def ListVectorGadgets():
    ListVectorWeapons()    
    ListVectorShields()                   

# GAME

print("Welcome to Sky Clash!!")

# I put some delay between each print output, so the user can read everything

time.sleep(2)
print()

AllStats() # showing each villain's health and energy
time.sleep(2)

ListGruGadgets()
time.sleep(2)
ListVectorGadgets()
time.sleep(2)

i = 1

while (P1.HP > 0 and P2.HP > 0) or (P1.energy < 20 and P2.energy < 15): 
    # The game will be looped until one of the villain's HP reaches zero
    # If both villians ran out of energy (which is a case I couldn't test)
    # then the HP will be the tiebreaker
    
    print("Begin fight round",i)
    i = i+1
    
    print()
    
    time.sleep(1)
    
    # At the start of each round, the damage dealt and cost will be set to zero
    
    P1_Weapon.damageto = 0
    P1_Weapon.costto = 0
    P2_Weapon.damageto = 0
    P2_Weapon.costto = 0
    P1_Shield.percentageto = 1
    P1_Shield.costto = 0
    P2_Shield.percentageto = 1  
    P2_Shield.costto = 0
    
    if Flag == 1: # A special case for the mega magnet weapon
        P1_Shield.percentageto = 20

    print("Gru's turn:")
    
    time.sleep(1)
    
    # At the start of each turn, each villian will be listed with his gadgets

    print("1. Freeze Gun")
    print("2. Electric Prod")
    print("3. Mega Magnet")
    print("4. Kalman Missile")
    print("5. Energy-Projected BarrierGun")
    print("6. Selective Permeability")
    print()
    
    time.sleep(1)

    op = int(input("Select gadget: "))
    
    time.sleep(0.7)
    
    # Depending on the gadget used, the cost and damage will be applied in the
    # damage dealt and cost variables
    
    # I apologize for the extreme redundancy, there was a bug with doing so while
    # defining my method and couldn't fix it on time

    if op == 1:
        if P1.energy >= Freeze_Gun.cost:
            Freeze_Gun.UseGadget()
            P1_Weapon.damageto = Freeze_Gun.damage
            P1_Weapon.costto = Freeze_Gun.cost
        else:
            print("Out of energy")    
    elif op == 2:
        if P1.energy >= Electric_Prod.cost:
            Electric_Prod.UseGadget()
            if Electric_Prod.quantity != 0:
                P1_Weapon.damageto = Electric_Prod.damage
                P1_Weapon.costto = Electric_Prod.cost
        else:
            print("Out of energy")        
    elif op == 3:
        if P1.energy >= Mega_Magnet.cost:
            Mega_Magnet.UseGadget()
            if Mega_Magnet.quantity != 0:
                P1_Weapon.damageto = Mega_Magnet.damage
                P1_Weapon.costto = Mega_Magnet.cost
        else:
            print("Out of energy")        
    elif op == 4: #Special
        if P1.energy >= Kalman_Missile.cost:
            Kalman_Missile.UseGadget()
            Kalman_Flag = 1
            if Kalman_Missile.quantity != 0:
                P2.HP = P2.HP - Kalman_Missile.damage # Direct hit
                P1_Weapon.costto = Kalman_Missile.cost 
        else:
            print("Out of energy")        
        
    elif op == 5:
        if P1.energy >= Energy_Projected_BarrierGun.cost:
            Energy_Projected_BarrierGun.UseGadget()
            P1_Shield.percentageto = Energy_Projected_BarrierGun.percentage/100
            P1_Shield.costto = Energy_Projected_BarrierGun.cost
        else:
            print("Out of energy")    
    elif op == 6:
        if P1.energy >= Selective_Permeability.cost:
            Selective_Permeability.UseGadget()
            if Selective_Permeability.quantity != 0:
                P1_Shield.percentageto = Selective_Permeability.percentage/100
                P1_Shield.costto = Selective_Permeability.cost
        else:
            print("Out of energy")        
            
    print()
    
    time.sleep(1)   
         
    print("Vector's turn")
    
    print("1. Laser Blasters")
    print("2. Plasma Grenades")
    print("3. Sonic Resonance Cannon")
    print("4. Energy Net Trap")
    print("5. Quantum Deflector")
    print()
    
    time.sleep(1)
    
    op = int(input("Select gadget: "))
    
    time.sleep(0.7)
    
    if op == 1:
        if P1.energy >= Laser_Blasters.cost:
            Laser_Blasters.UseGadget()
            P2_Weapon.damageto = Laser_Blasters.damage
            P2_Weapon.costto = Laser_Blasters.cost
        else:
            print("Out of energy")        
    elif op == 2:
        if P1.energy >= Plasma_Grenades.cost:
            Plasma_Grenades.UseGadget()
            if Plasma_Grenades.quantity != 0:
                P2_Weapon.damageto = Plasma_Grenades.damage
                P2_Weapon.costto = Plasma_Grenades.cost
        else:
            print("Out of energy")        
    elif op == 3:
        if P1.energy >= Sonic_Resonance_Cannon.cost:
            Sonic_Resonance_Cannon.UseGadget()
            if Sonic_Resonance_Cannon.quantity != 0:
                P2_Weapon.damageto = Sonic_Resonance_Cannon.damage
                P2_Weapon.costto = Sonic_Resonance_Cannon.cost
        else:
            print("Out of energy")        
        
    elif op == 4:
        if P1.energy >= Energy_Net_Trap.cost:
            Energy_Net_Trap.UseGadget()
            P2_Shield.percentageto = Energy_Net_Trap.percentage/100
            P2_Shield.costto = Energy_Net_Trap.cost
        else:
            print("Out of energy")        
    elif op == 5:
        if P1.energy >= Quantum_Deflector.cost:
            Quantum_Deflector.UseGadget()
            if Quantum_Deflector.quantity != 0:
                P2_Shield.percentageto = Quantum_Deflector.percentage/100
                P2_Shield.costto = Quantum_Deflector.cost
        else:
            print("Out of energy")        
    
    
    # Applying weapon damage and energy cost
    
    # If the villian used a weapon, the shield cost would be prerviously set to zero
    # Same thing goes for using a shield
    
    if Kalman_Flag == 1:
        P2_Shield.percentageto = 1
    
    P2.HP = P2.HP - (P1_Weapon.damageto * P2_Shield.percentageto)
    P1.HP = P1.HP - (P2_Weapon.damageto * P1_Shield.percentageto)
    
    P1.energy = P1.energy - P1_Weapon.costto - P1_Shield.costto
    P2.energy = P2.energy - P2_Weapon.costto - P2_Shield.costto
    
    time.sleep(2)
    
    print()
    
    # If the villian finally defeated the other one, the HP will be set to zero
    # so that it doesn't display negative numbers
    
    if P1.HP < 1:
        P1.HP = 0
    if P2.HP < 1:
        P2.HP = 0    
    if P1.energy < 1:
        P1.energy = 0
    if P2.energy < 1:
        P2.energy = 0    
    
    AllStats()
    
    time.sleep(2)
    
if P1.HP == P2.HP: # Rare case
    print("It's a draw")          
elif P1.HP > P2.HP:
    print("Gru wins!!")
elif P2.HP < P1.HP:
    print("Vector wins!!") 
    
elif P1.energy == 0 and P2.energy == 0: # Super rare case: tie breaker
    if P1.HP > P2.HP:
        print("Gru wins!!")
    else:
        print("Vector wins!!")    
        
# I could add more features like:
# -> The option of viewing the resources
# -> Reprompting if the player selected a gadget with high energy cost or out of resources
# I couldn't fully test it to check for bugs        