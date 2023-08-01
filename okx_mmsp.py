#!/usr/bin/python3
import okx.Account as Account
import okx.BlockTrading as BlockTrading
from okx.consts import *

# from absl import app
# from absl import flags
# from absl import logging

import argparse
import sys

parser = argparse.ArgumentParser(description='Process parameters.')
parser.add_argument('--credentials', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('--instFamily', type=str,  help='eg. BTC-USD')
parser.add_argument('--flag', type=int, default=0, help='eg. 0, 1')

# FLAGS = flags.FLAGS

# flags.DEFINE_string('okex_tx_apikey', None, 'okex_tx_apikey')
# flags.DEFINE_string('okex_tx_secret', None, 'okex_tx_secret')
# flags.DEFINE_string('okex_tx_passphrase', None, 'okex_tx_passphrase')
# flags.DEFINE_string('instFamily', None, 'BTC-USD, ETH-USD')



# Get positions history

GET_MMP = '/api/v5/account/mmp-config'
RESET_MMP = '/api/v5/account/mmp-reset'
params = {'instFamily': 'BTC-USD'}
params = {'instType': 'OPTION', 'instFamily': 'BTC-USD'}
# result = accountAPI._request_with_params(POST, RESET_MMP, params)
# result = BlockTradingAPI.reset_mmp()


args = parser.parse_args()
def getkeys(f):
    okex_tx_apikey = ''
    okex_tx_secret = ''
    okex_tx_passphrase = ''

    for raw in args.credentials.readlines():
        l = raw.strip()
        if 'okex_tx_apikey' in l:
            okex_tx_apikey = l.split('=')[1]
        elif 'okex_tx_secret' in l:
            okex_tx_secret = l.split('=')[1]
        elif 'okex_tx_passphrase' in l:
            okex_tx_passphrase = l.split('=')[1]
    return okex_tx_apikey.split(","), okex_tx_secret.split(","), okex_tx_passphrase.split(",")
        
def main():

    # apikeys = FLAGS.okex_tx_apikey.split(",");
    # secretkeys = FLAGS.okex_tx_secret(",");
    # passphrases = FLAGS.okex_tx_passphrase(",");
    apikeys, secretkeys, passphrases = getkeys(args.credentials)

    assert len(apikeys) == len(secretkeys) == len(passphrases)
    assert args.instFamily

    for count, apikey in enumerate(apikeys):
        # print(count, item, secretkeys[count], passphrases[count])
        secretkey = secretkeys[count]
        passphrase = passphrases[count] 
        accountAPI  = Account.AccountAPI(apikey, secretkey, passphrase, False, str(args.flag))
        result = accountAPI._request_with_params(GET, GET_MMP, params)
        print(result)

    exit(1)

if __name__ == '__main__':
    main()

