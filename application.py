def do_you_want_to_continue_func( keep_going = 1):
    
    try:
        keep_going = int(input('你還要繼續進行程式嗎?\n繼續請按1，停止請按0\n'))
        for keep_going in range (2):
            print('')
            
    except:
        print('輸入閣是錯誤，請再輸入一次\n')
        
    return keep_going

#do_you_want_to_continue_func()

def checking_func ( application_input , saving_length = 8 , english_lowercase = 1 , english_uppercase = 0 ,upper_equal_lower = True ,keep_going = True):

    '''
    application_input :要申請____的字串  
    saving_length     :預設 8.
    english_lowercase :預設 1.
    english_uppercase :預設 0.
    upper_equal_lower :True.(大小寫通用，以小寫為主)
    keep_going        :True.
'''    
    
    engApp = 0
    EngApp = 0   
    numApp = 0
    
    while keep_going == 1 :
        
        application_input = application_input.strip()
        
        # try:
        # 字元長度確認
        if len(application_input) < saving_length :
            keep_going = False
            print('字元需滿', saving_length ,'個字\n')
            continue
            
        elif len(application_input) > 20 :
            keep_going = False
            print('字元不得超過20個字\n')
            continue
        
        # 英文大小寫相關確認
        for i in range(len(application_input)):
            
            #英文小寫ASCII 97~122 
            if ord(application_input [i] ) in range(97,123):          
                engApp += 1  
            
            elif ord(application_input [i] ) in range(65,91):          
                EngApp += 1
                
            elif ord(application_input [i] ) in range(48,58):          
                numApp += 1
            
            else:
                print('請輸入正確格式')
                continue
            
            
        if  upper_equal_lower == False:
                
            if engApp < english_lowercase :
                print('英文小寫字數不符合要求')
                keep_going = False
                
                    
            if EngApp < english_uppercase :
                print('英文大寫字數不符合要求')
                keep_going = False
                
            
        else:
            if engApp + EngApp < english_lowercase + english_uppercase :
                print('英文字數不符合要求') 
                keep_going = False
                            
                    
            
        if keep_going == True :
            print (application_input,'符合申請格式')
            break
        
    return keep_going
   
checking_func('g12345678',8,1,0,1,1)


def application_main ( account, password, password_double_check, keep_going = 1 ):      
   
    while keep_going == True: 
    
       checking_func( account, 8, 1, 0, 1, 1) 
       #輸入密碼,字元長度,小寫,大寫,有分大小寫嗎,執行否
        
       if password != password_double_check :
            print('密碼與密碼確認不同\n')
            do_you_want_to_continue_func
        
       else :
            checking_func( password, 8, 1, 0, 0, 1)
            break
            
        
        
    return keep_going

acc_input = input('請輸入帳號')
pwd_input = input('請輸入密碼')
pwd_re  = input('請再次確認密碼')
application_main ( 'F129771057f', 'Aa841001' , 'Aa841001')