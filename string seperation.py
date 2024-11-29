if __name__ == '__main__':
    s='23424.123134'
    s = s.lstrip('0')
    
    
    if '.' in s:
        int_s, dec_s = s.split('.')
    else:
        int_s, dec_s = s,''
    
    int_s = ''.join(reversed(int_s))
    
    int_s = ','.join(int_s[i:i+3] for i in range(0,len(int_s),3))  
    
    int_s = ''.join(reversed(int_s))
    result = int_s + '.' + dec_s
    print(result)
    