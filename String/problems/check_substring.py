def substring(main:str, sub:str) -> bool:
    main_len = len(main)
    sub_len = len(sub)
    
    for i in range(main_len):
        if main[i: i+sub_len] == sub:
            return True
    return False

print(substring('hai izam', 'ai'))