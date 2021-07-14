from enum import Enum


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls, *include, exclude=None):
        """
        Returns a list of enum choices in the form (key, value).
        :param include: enum objs to include. If provided, only these choices
            will be included.
        :param exclude: a list of enum objs to exclude. If provided, only these
            choices will not be included, even if there were listed in the
            include param.
        """
        if exclude is None:
            exclude = []
        return [
            (key, obj.value) for key, obj in cls.__members__.items()
            if (not include or obj in include)
               and obj not in exclude
        ]

