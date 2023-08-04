from project.band_members.musician import Musician


class Drummer(Musician):
    def learn_new_skill(self, new_skill: str):
        TYPES_SKILLS = ["play the drums with drumsticks",
            "play the drums with drum brushes",
            "read sheet music",
        ]
        if new_skill not in TYPES_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise ValueError(f"{new_skill} is already learned!")

        self.skills.append(new_skill)

        return f"{self.name} learned to {new_skill}."
