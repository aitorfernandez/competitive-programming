#![allow(unused)]

pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        let mana = if self.level >= 10 { Some(100) } else { None };
        if self.health < 1 {
            Some(Self {
                health: 100,
                mana,
                level: self.level,
            })
        } else {
            None
        }
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        if let Some(mana) = self.mana {
            if mana > mana_cost {
                self.mana = Some(mana - mana_cost);
                mana_cost * 2
            } else {
                0
            }
        } else {
            self.health -= if self.health < mana_cost {
                self.health
            } else {
                mana_cost
            };
            0
        }
    }
}
