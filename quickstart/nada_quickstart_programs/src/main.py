from nada_dsl import *

def nada_main():
    # Define party
    party = Party(name="party1")

    # Define secret inputs (votes)
    vote_A = SecretInteger(Input(name="vote_A", party=party))
    vote_B = SecretInteger(Input(name="vote_B", party=party))
    vote_C = SecretInteger(Input(name="vote_C", party=party))
    vote_D = SecretInteger(Input(name="vote_D", party=party))    

    # Getting totall Votes
    total_vote = vote_A + vote_B + vote_C

    # Determining the average of the votes
    result = total_vote / vote_D

    # Outputs
    return [Output(result, "So the average of total vote is:", party)]