

def get_columns(type ='diab'):
    if type=='diab':
        columns = ['DID040','DIQ159', 'DIQ160', 'DIQ180','DIQ050','DID060','DIQ060U', 'DIQ065', 'DIQ070']
        diagnosis_column = 'DIQ010'
    elif type=='cvd':
        columns = ['MCQ160B','MCQ160D', 'MCQ160E', 'MCQ160F','MCQ160C']
        diagnosis_column = 'MCQ160C'
    elif type=='kidney_conditions':
        columns = ['KIQ025','KIQ005', 'KIQ010', 'KIQ042', 'KIQ044', 'KIQ048A', 'KIQ052', 'KIQ481']
        diagnosis_column = 'KIQ022'
    else:
        raise ValueError(f"Uncopported type {type}")
    
    return diagnosis_column, columns