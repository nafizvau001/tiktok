import requests

def tiktok():
    logo = ("""
                                                                                                                                                                                                                              
NNNNNNNN        NNNNNNNN               AAA               FFFFFFFFFFFFFFFFFFFFFFIIIIIIIIIIZZZZZZZZZZZZZZZZZZZ
N:::::::N       N::::::N              A:::A              F::::::::::::::::::::FI::::::::IZ:::::::::::::::::Z
N::::::::N      N::::::N             A:::::A             F::::::::::::::::::::FI::::::::IZ:::::::::::::::::Z
N:::::::::N     N::::::N            A:::::::A            FF::::::FFFFFFFFF::::FII::::::IIZ:::ZZZZZZZZ:::::Z 
N::::::::::N    N::::::N           A:::::::::A             F:::::F       FFFFFF  I::::I  ZZZZZ     Z:::::Z  
N:::::::::::N   N::::::N          A:::::A:::::A            F:::::F               I::::I          Z:::::Z    
N:::::::N::::N  N::::::N         A:::::A A:::::A           F::::::FFFFFFFFFF     I::::I         Z:::::Z     
N::::::N N::::N N::::::N        A:::::A   A:::::A          F:::::::::::::::F     I::::I        Z:::::Z      
N::::::N  N::::N:::::::N       A:::::A     A:::::A         F:::::::::::::::F     I::::I       Z:::::Z       
N::::::N   N:::::::::::N      A:::::AAAAAAAAA:::::A        F::::::FFFFFFFFFF     I::::I      Z:::::Z        
N::::::N    N::::::::::N     A:::::::::::::::::::::A       F:::::F               I::::I     Z:::::Z         
N::::::N     N:::::::::N    A:::::AAAAAAAAAAAAA:::::A      F:::::F               I::::I  ZZZ:::::Z     ZZZZZ
N::::::N      N::::::::N   A:::::A             A:::::A   FF:::::::FF           II::::::IIZ::::::ZZZZZZZZ:::Z
N::::::N       N:::::::N  A:::::A               A:::::A  F::::::::FF           I::::::::IZ:::::::::::::::::Z
N::::::N        N::::::N A:::::A                 A:::::A F::::::::FF           I::::::::IZ:::::::::::::::::Z
NNNNNNNN         NNNNNNNAAAAAAA                   AAAAAAAFFFFFFFFFFF           IIIIIIIIIIZZZZZZZZZZZZZZZZZZZ
                                                                                                            
                                                                                                            
                                                                                               
    """)
    print(logo)
    
    user_input = input('Enter Tiktok Username: ')
    url = f'http://localhost:8080/tiktok-info.php?username={user_input}'
    
    try:
        req = requests.get(url).json()
        
        print(req)
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

tiktok()
