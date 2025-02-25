import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name:str,position=(0,0)):
        match entity_name:
            case'Level1Bg':
                list_bg = []
                for i in range(7): # level 1 bg images number
                    list_bg.append(Background(f'Level1Bg{i}',position = (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}',position = (WIN_WIDTH, 0)))

                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(5):# level 2 bg images number
                    list_bg.append(Background(f'Level2Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', position=(WIN_WIDTH, 0)))

                return list_bg
            case 'Player1':
                return Player('Player1', position = (10,WIN_HEIGHT// 2 - 60))

            case 'Player2':
                return Player('Player2', position=(10, WIN_HEIGHT // 2 + 60))

            case 'Enemy1':
                return Enemy('Enemy1',(WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT -40)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))