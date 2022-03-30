pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        match self.health {
            0 => Some(Self {
                health: 100,
                mana: if self.level < 10 { None } else { Some(100) },
                ..*self
            }),
            _ => None,
        }
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        if let Some(m) = self.mana {
            match m >= mana_cost {
                true => {
                    self.mana = Some(m - mana_cost);
                    mana_cost * 2
                }
                false => 0,
            }
        } else {
            self.health = match self.health >= mana_cost {
                true => self.health - mana_cost,
                false => 0,
            };
            0
        }
    }
}
