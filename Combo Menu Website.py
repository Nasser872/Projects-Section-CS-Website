from ._anvil_designer import UITemplate
from anvil import *
import anvil.server
# Nasser did the code below
class UI(UITemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.orderBeef = []
    self.orderChicken = []
    self.orderTofu = []
    self.orderSmalld = []
    self.orderMediumd = []
    self.orderLarged = []
    self.orderSmallf = []
    self.orderMediumf = []
    self.orderLargef = []
    self.orderMegaf = []
    self.orderKetchup = []
    self.sandwichCost = 0
    self.beverageCost = 0
    self.friesCost = 0
    self.totalCost = 0
    self.ketchupCost = 0
  
  def Beef_click(self, **event_args):
    self.orderBeef.append("Beef Sandwich(es)")
    self.num_beef = len(self.orderBeef)
    self.Beefamount.text = self.num_beef
    self.sandwichCost += 6.25

  @handle("Chicken", "click")
  def Chicken_click(self, **event_args):
    self.orderChicken.append("Chicken Sandwich(es)")
    self.num_chicken = len(self.orderChicken)
    self.Chickenamount.text = self.num_chicken
    self.sandwichCost += 5.25

  @handle("Tofu", "click")
  def Tofu_click(self, **event_args):
    self.orderTofu.append("Tofu Sandwich(es)")
    self.num_tofu = len(self.orderTofu)
    self.Tofuamount.text = self.num_tofu
    self.sandwichCost += 5.75

  @handle("ResetS", "click")
  def ResetS_click(self, **event_args):
    self.orderBeef = []
    self.orderChicken = []
    self.orderTofu = []
    self.Beefamount.text = 0
    self.Chickenamount.text = 0
    self.Tofuamount.text = 0
    self.sandwichCost = 0

  @handle("SmallD", "click")
  def SmallD_click(self, **event_args):
    self.orderSmalld.append("Small Drink(s)")
    self.num_smalldrink = len(self.orderSmalld)
    self.smalldamount.text = self.num_smalldrink
    self.beverageCost += 1
    
  @handle("MediumD", "click")
  def MediumD_click(self, **event_args):
    self.orderMediumd.append("Medium Drink(s)")
    self.num_mediumdrink = len(self.orderMediumd)
    self.mediumdamount.text = self.num_mediumdrink
    self.beverageCost += 1.75

  @handle("LargeD", "click")
  def LargeD_click(self, **event_args):
    self.orderLarged.append("Large Drink(s)")
    self.num_largedrink = len(self.orderLarged)
    self.largedamount.text = self.num_largedrink
    self.beverageCost += 2.25

  @handle("ResetDrink", "click")
  def ResetDrink_click(self, **event_args):
    self.orderSmalld = []
    self.orderMediumd = []
    self.orderLarged = []
    self.smalldamount.text = 0
    self.mediumdamount.text = 0
    self.largedamount.text = 0
    self.beverageCost = 0

  @handle("SmallF", "click")
  def SmallF_click(self, **event_args):
    self.mega.visible = True
    self.MegaFy.visible = True
    self.MegaFn.visible = True

  @handle("MegaFy", "click")
  def MegaFy_click(self, **event_args):
    self.mega.visible = False
    self.MegaFy.visible = False
    self.MegaFn.visible = False
    self.orderMegaf.append("Mega Sized Fries")
    self.num_megafries = len(self.orderMegaf)
    self.Megaamount.text = self.num_megafries
    self.friesCost += 2

  @handle("MegaFn", "click")
  def MegaFn_click(self, **event_args):
    self.mega.visible = False
    self.MegaFy.visible = False
    self.MegaFn.visible = False
    self.orderSmallf.append("Small Fries")
    self.num_smallfries = len(self.orderSmallf)
    self.Smallfamount.text = self.num_smallfries
    self.friesCost += 1

  @handle("MediumF", "click")
  def MediumF_click(self, **event_args):
    self.orderMediumf.append("Medium Fries")
    self.num_mediumfries = len(self.orderMediumf)
    self.Mediumfamount.text = self.num_mediumfries
    self.friesCost += 1.50

  @handle("LargeF", "click")
  def LargeF_click(self, **event_args):
    self.orderLargef.append("Large Fries")
    self.num_largefries = len(self.orderLargef)
    self.Largefamount.text = self.num_largefries
    self.friesCost += 2

  @handle("Resetfries", "click")
  def Resetfries_click(self, **event_args):
    self.orderSmallf = []
    self.orderMediumf = []
    self.orderLargef = []
    self.orderMegaf = []
    self.Smallfamount.text = 0
    self.Mediumfamount.text = 0
    self.Largefamount.text = 0
    self.Megaamount.text = 0
    self.friesCost = 0
    
# Pranav did the code below
  @handle("packet", "click")
  def packet_click(self, **event_args):
    self.orderKetchup.append("Ketchup Packet(s)")
    self.num_ketchup = len(self.orderKetchup)
    self.packetamount.text = self.num_ketchup
    self.ketchupCost += 0.25

  @handle("Resetpackets", "click")
  def Resetpackets_click(self, **event_args):
    self.orderKetchup = []
    self.packetamount.text = 0
    self.ketchupCost = 0

  @handle("checkout", "click")
  def checkout_click(self, **event_args):
    self.outlined_card_1.visible = False
    self.outlined_card_2.visible = False
    self.outlined_card_3.visible = False
    self.outlined_card_4.visible = False
    self.checkout.visible = False
    self.totalCost = self.sandwichCost + self.beverageCost + self.friesCost + self.ketchupCost
    if self.sandwichCost > 0 and self.beverageCost > 0 and self.friesCost > 0:
      self.totalCost = self.totalCost - 1
      self.dollaroff.text = "Because you ordered a sandwich, fries, and drink, you got 1 dollar off on your order!"
    self.totalcost.text = "Your final cost is: $" + str(self.totalCost)
    self.finalSandwiches = list(set(self.orderBeef + self.orderChicken + self.orderTofu))
    for sandwich in self.finalSandwiches:
      self.label_7.text = self.label_7.text + sandwich + "\n"
    if len(self.orderBeef) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderBeef)) + "\n"
    if len(self.orderChicken) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderChicken)) + "\n"
    if len(self.orderTofu) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderTofu)) + "\n"
    self.finalDrinks = list(set(self.orderSmalld + self.orderMediumd + self.orderLarged))
    for drink in self.finalDrinks:
      self.label_7.text = self.label_7.text + drink + "\n"
    if len(self.orderSmalld) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderSmalld)) + "\n"
    if len(self.orderMediumd) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderMediumd)) + "\n"
    if len(self.orderLarged) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderLarged)) + "\n"
    self.finalFries = list(set(self.orderSmallf + self.orderMediumf + self.orderLargef + self.orderMegaf))
    for fries in self.finalFries:
      self.label_7.text = self.label_7.text + fries + "\n"
    if len(self.orderSmallf) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderSmallf)) + "\n"
    if len(self.orderMediumf) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderMediumf)) + "\n"
    if len(self.orderLargef) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderLargef)) + "\n"
    if len(self.orderMegaf) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderMegaf)) + "\n"
    if len(self.orderKetchup) > 0:
      self.label_6.text = self.label_6.text + str(len(self.orderKetchup)) + "\n"
      self.label_7.text = self.label_7.text + "Ketchup Packet(s)"
    

  

  
  

  
    
    
  

    

