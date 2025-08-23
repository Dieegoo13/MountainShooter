from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left > WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(entity1, entity2):
        valid_interaction = False
        if isinstance(entity1, Enemy) and isinstance(entity2, PlayerShot):
            valid_interaction = True
        elif isinstance(entity1, PlayerShot) and isinstance(entity2, Enemy):
            valid_interaction = True
        elif isinstance(entity1, Player) and isinstance(entity2, EnemyShot):
            valid_interaction = True
        elif isinstance(entity1, EnemyShot) and isinstance(entity2, Player):
            valid_interaction = True

        if valid_interaction:
            if (entity1.rect.right >= entity2.rect.left and entity1.rect.left <= entity2.rect.right
                    and entity1.rect.bottom >= entity2.rect.top
                    and entity1.rect.top <= entity2.rect.bottom):

                if entity1.health is None:
                    entity1.health = 0
                if entity2.health is None:
                    entity2.health = 0

                dmg1 = entity2.damage if entity2.damage is not None else 0
                dmg2 = entity1.damage if entity1.damage is not None else 0

                entity1.health -= dmg1
                entity2.health -= dmg2

                entity1.last_dmg = getattr(entity2, "name", "Unknown")
                entity2.last_dmg = getattr(entity1, "name", "Unknown")

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.score is None:  # proteção extra
            enemy.score = 0

        for entity in entity_list:
            if isinstance(entity, Player):
                if entity.score is None:  # proteção extra
                    entity.score = 0

                if enemy.last_dmg == 'Player1Shot.png' and entity.name == 'Player1.png':
                    entity.score += enemy.score
                elif enemy.last_dmg == 'Player2Shot.png' and entity.name == 'Player2.png':
                    entity.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in list(entity_list):
            if ent.health is not None and ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                if not isinstance(ent, Player):
                    entity_list.remove(ent)
                else:

                    ent.health = max(ent.health, 0)