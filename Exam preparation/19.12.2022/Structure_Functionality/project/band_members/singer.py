from project.band_members.musician import Musician


class Singer(Musician):
    # def available_types_of_skills(self):
    #     return [
    #         "sing high pitch notes",
    #         "sing low pitch notes"
    #     ]
    #
    # def learn_new_skill(self, new_skill: str):
    #     super().learn_new_skill(new_skill)

    def learn_new_skill(self, new_skill: str):
        TYPES_SKILLS = [
            "sing high pitch notes",
            "sing low pitch notes"
        ]
        if new_skill not in TYPES_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise ValueError(f"{new_skill} is already learned!")

        self.skills.append(new_skill)

        return f"{self.name} learned to {new_skill}."

