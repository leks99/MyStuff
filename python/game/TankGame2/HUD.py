class HUD:
    def __init__(self, font):
        self.font = font
    def draw(self, allList, display):
        #  player HP
        playerHPtext = "HP " + str(allList[0].hp)
        playerHP = self.font.render(playerHPtext, False, (0, 0, 160))
        display.blit(playerHP, (15, 0))
        #  player Ammo
        playerAmmotext = "ammo " + str(allList[0].ammo)
        playerAmmo = self.font.render(playerAmmotext, False, (0, 0, 160))
        display.blit(playerAmmo, (5, 40))
        #  enemy HP
        enemyHPtext = "HP " + str(allList[1].hp)
        enemyHP = self.font.render(enemyHPtext, False, (160, 0, 0))
        display.blit(enemyHP, (1750, 0))
        #  enemy Ammo
        enemyAmmotext = "ammo " + str(allList[1].ammo)
        enemyAmmo = self.font.render(enemyAmmotext, False, (160, 0, 0))
        display.blit(enemyAmmo, (1740, 40))