class Global :
    __team_number_count : int = 2

    @classmethod
    def Set_team_number_count(cls, value: int):
        set_value = cls.__team_number_count + value
        cls.__team_number_count = max(2, min(value, 9))

    @classmethod
    def Get_team_number_count(cls) :
        return cls.__team_number_count