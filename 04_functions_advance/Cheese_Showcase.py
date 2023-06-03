def sorting_cheeses(**kwargs):
    result = ""
    for cheese, quantities in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{cheese}\n" + "\n".join(str(x) for x in sorted(quantities, reverse=True)) + "\n"
    return result