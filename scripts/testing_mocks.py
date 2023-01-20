import json
import time
mock_prod_markup = {
    'optimal_base_markup':{
        'test':{
            'airport':{
                'd1':5,
                'd2':12,
                'd3':14
            },
            'common':{
                'd1':3,
                'd2':4,
                'd3':5
            },
        }
    }
}

mock_treat_markup = {
    'optimal_base_markup':{
        'test':{
            'airport_pick_up':{
                'd1':4,
                'd2':1,
                'd3':416
            },
            'common':{
                'd1':2,
                'd2':4,
                'd3':52
            },
        }
    }
}

mock_prod_pt = {
    'targets': {
        'test': {
            'targets': [
                {
                    'use_case_i':'airport',
                    'use_case_j':'d1',
                    'lower_limit_cents':2,
                    'upper_limit_cents':2
                },
                {
                    'use_case_i':'airport',
                    'use_case_j':'d2',
                    'lower_limit_cents':3,
                    'upper_limit_cents':3
                },
                {
                    'use_case_i':'airport',
                    'use_case_j':'d3',
                    'lower_limit_cents':4,
                    'upper_limit_cents':4
                },
                {
                    'use_case_i':'common',
                    'use_case_j':'d1',
                    'lower_limit_cents':52,
                    'upper_limit_cents':52
                },
                {
                    'use_case_i':'common',
                    'use_case_j':'d2',
                    'lower_limit_cents':53,
                    'upper_limit_cents':53
                },
                {
                    'use_case_i':'common',
                    'use_case_j':'d3',
                    'lower_limit_cents':61,
                    'upper_limit_cents':61
                }
            ]
        }
    }
}

mock_treat_pt = {
    'targets': {
        'test': {
            'targets': [
                {
                    'use_case_i':'airport_pick_up',
                    'use_case_j':'d1',
                    'lower_limit_cents':35,
                    'upper_limit_cents':35
                },
                {
                    'use_case_i':'airport_pick_up',
                    'use_case_j':'d2',
                    'lower_limit_cents':235,
                    'upper_limit_cents':235
                },
                {
                    'use_case_i':'airport_pick_up',
                    'use_case_j':'d3',
                    'lower_limit_cents':2,
                    'upper_limit_cents':2
                },
                {
                    'use_case_i':'common',
                    'use_case_j':'d1',
                    'lower_limit_cents':2,
                    'upper_limit_cents':2
                },
                {
                    'use_case_i':'common',
                    'use_case_j':'d2',
                    'lower_limit_cents':256,
                    'upper_limit_cents':256
                },
                {
                    'use_case_i':'common',
                    'use_case_j':'d3',
                    'lower_limit_cents':231,
                    'upper_limit_cents':231
                }
            ]
        }
    }
}

mock_prod_markup_str = json.dumps(mock_prod_markup)
mock_treat_markup_str = json.dumps(mock_treat_markup)
mock_prod_pt_str = json.dumps(mock_prod_pt)
mock_treat_pt_str = json.dumps(mock_treat_pt)