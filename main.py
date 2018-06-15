# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:58:21 2018

@author: Fran
"""

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random






#Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")


#White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

#Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 1000)
special = Item("Especial Potion", "potion", "Heals 5000 HP", 5000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega Elixer","elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade","attack","Deals 500 damage", 500)


#Initiate People
player_spells = [fire,thunder,blizzard,meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenade, "quantity": 5}]

enemy_items = [{"item": special, "quantity": 2},
               {"item": elixer, "quantity": 1}]

player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick: ", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)

enemy2 =  Person("Imp:    ", 1250, 130, 560, 325, [],[])
enemy1 =  Person("Magus:", 11200, 701, 525, 25, [],enemy_items)
enemy3 =  Person("Imp:    ", 1250, 130, 560, 325, [],[])

players = [player1, player2, player3]
enemies = [enemy2, enemy1, enemy3]
running = True
i= 0
print("\n")
print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!" + bcolors.ENDC)


while running:
    players = player1.people_alive(players)
    enemies = enemy1.people_alive(enemies)
    print("=====================================")
    print("\n\n")
    print("NAME                           HP                                    MP")
    for player in players:
      
      player.get_stats()
      print("\n")
    for enemy in enemies:
      enemy.get_enemy_stats()

    for player in players:
      player.choose_action()
      choice = input("Choose Action: ")
      index = int(choice) - 1
      print("You chose " + player.actions[index])
      
      if index == 3:
          break
      
      if index == 0: #Attack
          dmg = player.generate_damage()
          enemy = player.choose_target(enemies)
          enemies[enemy].take_damage(dmg)
          print("You attacked " + enemies[enemy].name + " for " + bcolors.BOLD + bcolors.FAIL + str(dmg)+ bcolors.ENDC + " points of damage.")
      
      elif index == 1: #Magic
          player.choose_magic()
          magic_choice = int(input("Choose Spell: ")) - 1
          
          if magic_choice == -1:
              continue

          
          spell = player.magic[magic_choice]
          magic_dmg = spell.generate_damage()
          
          current_mg = player.get_mp()
          
          if spell.cost > current_mg:
              print (bcolors.FAIL + "\n Not engough MP\n" +bcolors.ENDC)
              continue
          
          player.reduce_mp(spell.cost)
          if spell.type == "white":
              player.heal(magic_dmg)
              print("Player heals for " + str(magic_dmg))
          elif spell.type == "black":
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg) + " Points of damage to " + enemies[enemy].name + bcolors.ENDC)
                
          
      elif index == 2: #Item
          player.choose_item()
          item_choice = int(input("Choose Item: ")) - 1
          
          if item_choice == -1:
              continue
          
          item = player.items[item_choice]["item"]
          if player.items[item_choice]["quantity"] == -0:
              print(bcolors.FAIL + "\n" + "None left... " + bcolors.ENDC)
              continue
          
          player.items[item_choice]["quantity"] -= 1
          
          
          
          
          if item.type == "potion":
              player.heal(item.prop)
              print(bcolors.OKGREEN + "\n" + str(item.name) + "heals for: " + str(item.prop) + "HP" + bcolors.ENDC)
          elif item.type == "elixer":

            if item.name == "Mega Elixer":
              for i in players:
                player.hp = i.maxhp
                player.mp = i.maxmp

            else:
              player.hp = player.maxhp
              player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + str(item.name) + "fully restores HP and MP" + bcolors.ENDC)
          elif item.type == "attack":
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(item.prop)
            print(bcolors.FAIL + "\n" + str(item.name) + "deals " + str(item.prop) + " points of dmg to " + enemies[enemy].name + bcolors.ENDC)
      
      '''
      defeated_enemies = 0
      for enemy in enemies:
        if enemy.get_hp() == 0:
          defeated_enemies+=1

        if defeated_enemies == 2:
          print(bcolors.OKGREEN + "Enemies died. You won!" + bcolors.ENDC)
          running = False
          break
        '''

      
      

    for enemy in enemies:
        enemy_action = 0
        if enemy.name == "Magus:":

            if enemy.get_hp() < (enemy.get_max_hp() / 3):
                if enemy.has_elixer():
                    heal_mp = random.randrange(0, 100)
                    if heal_mp > 69:
                        enemy_action = 1

            if enemy.get_hp() < (enemy.get_max_hp()/2):
                if enemy.has_potions():
                    heal = random.randrange(0,100)
                    if heal > 50:
                        enemy_action = 2




        if enemy_action == 0: #Attack
            enemy_choice = 1
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(bcolors.BOLD + enemy.name + bcolors.ENDC + " attacks " + bcolors.BOLD + players[target].name + bcolors.ENDC + "for " + str(enemy_dmg))


        if enemy_action == 1: #Magnus heals completely
            enemy.hp = enemy.get_maxhp
            enemy.mp = enemy.maxmp
            print(bcolors.BOLD + bcolors.FAIL + enemy.name + " has recovered completely")
        if enemy_action == 2: #Magus heals
            item = enemy.items[0]["item"]
            enemy.heal(item.prop)
            print(bcolors.FAIL + "\n" + enemy.name + "uses " + str(item.name) + " and heals for: " + str(item.prop) + "HP" + bcolors.ENDC)
    if len(players) == 0:
        print(bcolors.FAIL + "You ran out of players. " + bcolors.BOLD + "You died :( " + bcolors.ENDC )
        running = False
        break
    if len(enemies) == 0:
        print(bcolors.OKGREEN + "You defeated all the enemies. " + bcolors.BOLD + "YOU WON!" + bcolors.ENDC)
   
    