from typing import Callable, Dict, List, TypeVar

base_phare = [
    "três",       # 0
    "pratos",     # 1
    "de",         # 2
    "trigo",      # 3
    "para",       # 4
    "três",       # 5
    "tigres",     # 6
    "tristes",    # 7
]

PhraseModifier = Callable[[List[str]], List[str]]


def make_changer(pos: int, new_value: str) -> Callable[[List[str]], List[str]]:
    def change(previous_value: List[str]) -> List[str]:
        new_phrase = [*previous_value] # copy
        new_phrase[pos] = new_value
        return new_phrase

    return change


phrase_modifiers: Dict[str, PhraseModifier] = {
    "primeiro_três_para_tres": make_changer(0, "tres"),
    "segundo_três_para_tres": make_changer(5, "tres"),
    "para_para_pra": make_changer(4, "pra"),
}


T = TypeVar("T")


def combs(a: List[T]) -> List[List[T]]:
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c + [a[0]]]
    return cs


generated = combs(list(phrase_modifiers.keys()))


def main() -> None:
    combination_results: Dict[str, List[str]] = {}

    for combination in generated:
        phrase = base_phare
        for modifier in combination:
            phrase = phrase_modifiers[modifier](phrase)
        combination_results[", ".join(combination)] = phrase

    for combination_key, result in combination_results.items():
        print(
            " ".join(
                [
                    f"[{combination_key}]:",
                    (" ".join(result)),
                ]
            )
        )


if __name__ == "__main__":
    main()
