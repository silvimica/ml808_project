

def get_columns(type ='diabetes'):
    if type=='diabetes':
        columns = ['DID040','DIQ159', 'DIQ160', 'DIQ180','DIQ050','DID060','DIQ060U', 'DIQ065', 'DIQ070']
        diagnosis_column = 'DIQ010'
    if type=='cvd':
        columns = ['MCQ160b','MCQ160d', 'MCQ160e', 'MCQ160f']
        diagnosis_column = 'MCQ160c'
    if type=='kidney_conditions':
        columns = ['KIQ025','KIQ005', 'KIQ010', 'KIQ042', 'KIQ044', 'KIQ048A', 'KIQ052', 'KIQ481']
        diagnosis_column = 'KIQ022'
    else:
        raise ValueError(f"Uncopported type {type}")
    
    return diagnosis_column, columns