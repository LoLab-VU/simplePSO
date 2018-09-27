# exported from PySB model 'earm.lopez_embedded'

from pysb import Model, Monomer, Parameter, Rule, Observable, Initial, \
    Annotation, \
    MatchOnce

Model()

Monomer('L', ['bf'])
Monomer('R', ['bf'])
Monomer('DISC', ['bf'])
Monomer('flip', ['bf'])
Monomer('C8', ['bf', 'state'], {'state': ['pro', 'A']})
Monomer('BAR', ['bf'])
Monomer('Bid', ['bf', 'state'], {'state': ['U', 'T', 'M']})
Monomer('Bax', ['bf', 's1', 's2', 'state'], {'state': ['C', 'M', 'A']})
Monomer('Bak', ['bf', 's1', 's2', 'state'], {'state': ['M', 'A']})
Monomer('Bcl2', ['bf', 'state'], {'state': ['C', 'M']})
Monomer('BclxL', ['bf', 'state'], {'state': ['C', 'M']})
Monomer('Mcl1', ['bf', 'state'], {'state': ['C', 'M']})
Monomer('Bad', ['bf', 'state'], {'state': ['C', 'M']})
Monomer('Noxa', ['bf', 'state'], {'state': ['C', 'M']})
Monomer('CytoC', ['bf', 'state'], {'state': ['M', 'C', 'A']})
Monomer('Smac', ['bf', 'state'], {'state': ['M', 'C', 'A']})
Monomer('Apaf', ['bf', 'state'], {'state': ['I', 'A']})
Monomer('Apop', ['bf'])
Monomer('C3', ['bf', 'state'], {'state': ['pro', 'A', 'ub']})
Monomer('C6', ['bf', 'state'], {'state': ['pro', 'A']})
Monomer('C9', ['bf'])
Monomer('PARP', ['bf', 'state'], {'state': ['U', 'C']})
Monomer('XIAP', ['bf'])

Parameter('L_0', 3000.0)
Parameter('R_0', 200.0)
Parameter('Flip_0', 100.0)
Parameter('C8_0', 20000.0)
Parameter('BAR_0', 1000.0)
Parameter('bind_L_R_to_LR_kf', 4e-07)
Parameter('bind_L_R_to_LR_kr', 0.001)
Parameter('convert_LR_to_DISC_kc', 1e-05)
Parameter('bind_DISC_C8pro_to_DISCC8pro_kf', 1e-06)
Parameter('bind_DISC_C8pro_to_DISCC8pro_kr', 0.001)
Parameter('catalyze_DISCC8pro_to_DISC_C8A_kc', 1.0)
Parameter('bind_C8A_BidU_to_C8ABidU_kf', 1e-06)
Parameter('bind_C8A_BidU_to_C8ABidU_kr', 0.001)
Parameter('catalyze_C8ABidU_to_C8A_BidT_kc', 1.0)
Parameter('bind_DISC_flip_kf', 1e-06)
Parameter('bind_DISC_flip_kr', 0.001)
Parameter('bind_BAR_C8A_kf', 1e-06)
Parameter('bind_BAR_C8A_kr', 0.001)
Parameter('Apaf_0', 100000.0)
Parameter('C3_0', 10000.0)
Parameter('C6_0', 10000.0)
Parameter('C9_0', 100000.0)
Parameter('XIAP_0', 100000.0)
Parameter('PARP_0', 1000000.0)
Parameter('equilibrate_SmacC_to_SmacA_kf', 0.01)
Parameter('equilibrate_SmacC_to_SmacA_kr', 0.01)
Parameter('equilibrate_CytoCC_to_CytoCA_kf', 0.01)
Parameter('equilibrate_CytoCC_to_CytoCA_kr', 0.01)
Parameter('bind_CytoCA_ApafI_to_CytoCAApafI_kf', 5e-07)
Parameter('bind_CytoCA_ApafI_to_CytoCAApafI_kr', 0.001)
Parameter('catalyze_CytoCAApafI_to_CytoCA_ApafA_kc', 1.0)
Parameter('convert_ApafA_C9_to_Apop_kf', 5e-08)
Parameter('convert_ApafA_C9_to_Apop_kr', 0.001)
Parameter('bind_Apop_C3pro_to_ApopC3pro_kf', 5e-09)
Parameter('bind_Apop_C3pro_to_ApopC3pro_kr', 0.001)
Parameter('catalyze_ApopC3pro_to_Apop_C3A_kc', 1.0)
Parameter('bind_Apop_XIAP_kf', 2e-06)
Parameter('bind_Apop_XIAP_kr', 0.001)
Parameter('bind_SmacA_XIAP_kf', 7e-06)
Parameter('bind_SmacA_XIAP_kr', 0.001)
Parameter('bind_C8A_C3pro_to_C8AC3pro_kf', 1e-07)
Parameter('bind_C8A_C3pro_to_C8AC3pro_kr', 0.001)
Parameter('catalyze_C8AC3pro_to_C8A_C3A_kc', 1.0)
Parameter('bind_XIAP_C3A_to_XIAPC3A_kf', 2e-06)
Parameter('bind_XIAP_C3A_to_XIAPC3A_kr', 0.001)
Parameter('catalyze_XIAPC3A_to_XIAP_C3ub_kc', 0.1)
Parameter('bind_C3A_PARPU_to_C3APARPU_kf', 1e-06)
Parameter('bind_C3A_PARPU_to_C3APARPU_kr', 0.01)
Parameter('catalyze_C3APARPU_to_C3A_PARPC_kc', 1.0)
Parameter('bind_C3A_C6pro_to_C3AC6pro_kf', 1e-06)
Parameter('bind_C3A_C6pro_to_C3AC6pro_kr', 0.001)
Parameter('catalyze_C3AC6pro_to_C3A_C6A_kc', 1.0)
Parameter('bind_C6A_C8pro_to_C6AC8pro_kf', 3e-08)
Parameter('bind_C6A_C8pro_to_C6AC8pro_kr', 0.001)
Parameter('catalyze_C6AC8pro_to_C6A_C8A_kc', 1.0)
Parameter('Bid_0', 40000.0)
Parameter('BclxL_0', 20000.0)
Parameter('Mcl1_0', 20000.0)
Parameter('Bcl2_0', 20000.0)
Parameter('Bad_0', 1000.0)
Parameter('Noxa_0', 1000.0)
Parameter('CytoC_0', 500000.0)
Parameter('Smac_0', 100000.0)
Parameter('Bax_0', 80000.0)
Parameter('Bak_0', 20000.0)
Parameter('equilibrate_BidT_to_BidM_kf', 0.1)
Parameter('equilibrate_BidT_to_BidM_kr', 0.001)
Parameter('bind_BidM_BaxC_to_BidMBaxC_kf', 1e-07)
Parameter('bind_BidM_BaxC_to_BidMBaxC_kr', 0.001)
Parameter('catalyze_BidMBaxC_to_BidM_BaxM_kc', 1.0)
Parameter('bind_BidM_BaxM_to_BidMBaxM_kf', 1e-07)
Parameter('bind_BidM_BaxM_to_BidMBaxM_kr', 0.001)
Parameter('catalyze_BidMBaxM_to_BidM_BaxA_kc', 1.0)
Parameter('bind_BidM_BakM_to_BidMBakM_kf', 1e-07)
Parameter('bind_BidM_BakM_to_BidMBakM_kr', 0.001)
Parameter('catalyze_BidMBakM_to_BidM_BakA_kc', 1.0)
Parameter('bind_BaxA_BaxM_to_BaxABaxM_kf', 1e-07)
Parameter('bind_BaxA_BaxM_to_BaxABaxM_kr', 0.001)
Parameter('catalyze_BaxABaxM_to_BaxA_BaxA_kc', 1.0)
Parameter('bind_BakA_BakM_to_BakABakM_kf', 1e-07)
Parameter('bind_BakA_BakM_to_BakABakM_kr', 0.001)
Parameter('catalyze_BakABakM_to_BakA_BakA_kc', 1.0)
Parameter('bind_BidM_Bcl2M_kf', 1e-06)
Parameter('bind_BidM_Bcl2M_kr', 0.06600000000000002)
Parameter('bind_BidM_BclxLM_kf', 1e-06)
Parameter('bind_BidM_BclxLM_kr', 0.012000000000000002)
Parameter('bind_BidM_Mcl1M_kf', 1e-06)
Parameter('bind_BidM_Mcl1M_kr', 0.010000000000000002)
Parameter('bind_BaxA_Bcl2_kf', 1e-06)
Parameter('bind_BaxA_Bcl2_kr', 0.010000000000000002)
Parameter('bind_BaxA_BclxLM_kf', 1e-06)
Parameter('bind_BaxA_BclxLM_kr', 0.010000000000000002)
Parameter('bind_BakA_BclxLM_kf', 1e-06)
Parameter('bind_BakA_BclxLM_kr', 0.05)
Parameter('bind_BakA_Mcl1M_kf', 1e-06)
Parameter('bind_BakA_Mcl1M_kr', 0.010000000000000002)
Parameter('bind_BadM_Bcl2M_kf', 1e-06)
Parameter('bind_BadM_Bcl2M_kr', 0.011000000000000001)
Parameter('bind_BadM_BclxLM_kf', 1e-06)
Parameter('bind_BadM_BclxLM_kr', 0.010000000000000002)
Parameter('bind_NoxaM_Mcl1M_kf', 1e-06)
Parameter('bind_NoxaM_Mcl1M_kr', 0.019000000000000006)
Parameter('assemble_pore_sequential_Bax_2_kf', 0.0002040816)
Parameter('assemble_pore_sequential_Bax_2_kr', 0.001)
Parameter('assemble_pore_sequential_Bax_3_kf', 0.0002040816)
Parameter('assemble_pore_sequential_Bax_3_kr', 0.001)
Parameter('assemble_pore_sequential_Bax_4_kf', 0.0002040816)
Parameter('assemble_pore_sequential_Bax_4_kr', 0.001)
Parameter('assemble_pore_sequential_Bak_2_kf', 0.0002040816)
Parameter('assemble_pore_sequential_Bak_2_kr', 0.001)
Parameter('assemble_pore_sequential_Bak_3_kf', 0.0002040816)
Parameter('assemble_pore_sequential_Bak_3_kr', 0.001)
Parameter('assemble_pore_sequential_Bak_4_kf', 0.0002040816)
Parameter('assemble_pore_sequential_Bak_4_kr', 0.001)
Parameter('pore_transport_complex_BaxA_4_CytoCM_kf', 2.857143e-05)
Parameter('pore_transport_complex_BaxA_4_CytoCM_kr', 0.001)
Parameter('pore_transport_dissociate_BaxA_4_CytoCC_kc', 10.0)
Parameter('pore_transport_complex_BaxA_4_SmacM_kf', 2.857143e-05)
Parameter('pore_transport_complex_BaxA_4_SmacM_kr', 0.001)
Parameter('pore_transport_dissociate_BaxA_4_SmacC_kc', 10.0)
Parameter('pore_transport_complex_BakA_4_CytoCM_kf', 2.857143e-05)
Parameter('pore_transport_complex_BakA_4_CytoCM_kr', 0.001)
Parameter('pore_transport_dissociate_BakA_4_CytoCC_kc', 10.0)
Parameter('pore_transport_complex_BakA_4_SmacM_kf', 2.857143e-05)
Parameter('pore_transport_complex_BakA_4_SmacM_kr', 0.001)
Parameter('pore_transport_dissociate_BakA_4_SmacC_kc', 10.0)

Observable('mBid', Bid(state='M'))
Observable('aSmac', Smac(state='A'))
Observable('cPARP', PARP(state='C'))

Rule('bind_L_R_to_LR', L(bf=None) + R(bf=None) | L(bf=1) % R(bf=1),
     bind_L_R_to_LR_kf, bind_L_R_to_LR_kr)
Rule('convert_LR_to_DISC', L(bf=1) % R(bf=1) >> DISC(bf=None),
     convert_LR_to_DISC_kc)
Rule('bind_DISC_C8pro_to_DISCC8pro',
     DISC(bf=None) + C8(bf=None, state='pro') <> DISC(bf=1) % C8(bf=1,
                                                                 state='pro'),
     bind_DISC_C8pro_to_DISCC8pro_kf, bind_DISC_C8pro_to_DISCC8pro_kr)
Rule('catalyze_DISCC8pro_to_DISC_C8A',
     DISC(bf=1) % C8(bf=1, state='pro') >> DISC(bf=None) + C8(bf=None,
                                                              state='A'),
     catalyze_DISCC8pro_to_DISC_C8A_kc)
Rule('bind_C8A_BidU_to_C8ABidU',
     C8(bf=None, state='A') + Bid(bf=None, state='U') | C8(bf=1,
                                                           state='A') % Bid(
         bf=1, state='U'), bind_C8A_BidU_to_C8ABidU_kf,
     bind_C8A_BidU_to_C8ABidU_kr)
Rule('catalyze_C8ABidU_to_C8A_BidT',
     C8(bf=1, state='A') % Bid(bf=1, state='U') >> C8(bf=None,
                                                      state='A') + Bid(bf=None,
                                                                       state='T'),
     catalyze_C8ABidU_to_C8A_BidT_kc)
Rule('bind_DISC_flip',
     DISC(bf=None) + flip(bf=None) <> DISC(bf=1) % flip(bf=1),
     bind_DISC_flip_kf, bind_DISC_flip_kr)
Rule('bind_BAR_C8A',
     BAR(bf=None) + C8(bf=None, state='A') | BAR(bf=1) % C8(bf=1, state='A'),
     bind_BAR_C8A_kf, bind_BAR_C8A_kr)
Rule('equilibrate_SmacC_to_SmacA',
     Smac(bf=None, state='C') | Smac(bf=None, state='A'),
     equilibrate_SmacC_to_SmacA_kf, equilibrate_SmacC_to_SmacA_kr)
Rule('equilibrate_CytoCC_to_CytoCA',
     CytoC(bf=None, state='C') | CytoC(bf=None, state='A'),
     equilibrate_CytoCC_to_CytoCA_kf, equilibrate_CytoCC_to_CytoCA_kr)
Rule('bind_CytoCA_ApafI_to_CytoCAApafI',
     CytoC(bf=None, state='A') + Apaf(bf=None, state='I') | CytoC(bf=1,
                                                                  state='A') % Apaf(
         bf=1, state='I'), bind_CytoCA_ApafI_to_CytoCAApafI_kf,
     bind_CytoCA_ApafI_to_CytoCAApafI_kr)
Rule('catalyze_CytoCAApafI_to_CytoCA_ApafA',
     CytoC(bf=1, state='A') % Apaf(bf=1, state='I') >> CytoC(bf=None,
                                                             state='A') + Apaf(
         bf=None, state='A'), catalyze_CytoCAApafI_to_CytoCA_ApafA_kc)
Rule('convert_ApafA_C9_to_Apop',
     Apaf(bf=None, state='A') + C9(bf=None) | Apop(bf=None),
     convert_ApafA_C9_to_Apop_kf, convert_ApafA_C9_to_Apop_kr)
Rule('bind_Apop_C3pro_to_ApopC3pro',
     Apop(bf=None) + C3(bf=None, state='pro') | Apop(bf=1) % C3(bf=1,
                                                                state='pro'),
     bind_Apop_C3pro_to_ApopC3pro_kf, bind_Apop_C3pro_to_ApopC3pro_kr)
Rule('catalyze_ApopC3pro_to_Apop_C3A',
     Apop(bf=1) % C3(bf=1, state='pro') >> Apop(bf=None) + C3(bf=None,
                                                              state='A'),
     catalyze_ApopC3pro_to_Apop_C3A_kc)
Rule('bind_Apop_XIAP',
     Apop(bf=None) + XIAP(bf=None) | Apop(bf=1) % XIAP(bf=1),
     bind_Apop_XIAP_kf, bind_Apop_XIAP_kr)
Rule('bind_SmacA_XIAP',
     Smac(bf=None, state='A') + XIAP(bf=None) | Smac(bf=1, state='A') % XIAP(
         bf=1), bind_SmacA_XIAP_kf, bind_SmacA_XIAP_kr)
Rule('bind_C8A_C3pro_to_C8AC3pro',
     C8(bf=None, state='A') + C3(bf=None, state='pro') | C8(bf=1,
                                                            state='A') % C3(
         bf=1, state='pro'), bind_C8A_C3pro_to_C8AC3pro_kf,
     bind_C8A_C3pro_to_C8AC3pro_kr)
Rule('catalyze_C8AC3pro_to_C8A_C3A',
     C8(bf=1, state='A') % C3(bf=1, state='pro') >> C8(bf=None,
                                                       state='A') + C3(bf=None,
                                                                       state='A'),
     catalyze_C8AC3pro_to_C8A_C3A_kc)
Rule('bind_XIAP_C3A_to_XIAPC3A',
     XIAP(bf=None) + C3(bf=None, state='A') | XIAP(bf=1) % C3(bf=1,
                                                              state='A'),
     bind_XIAP_C3A_to_XIAPC3A_kf, bind_XIAP_C3A_to_XIAPC3A_kr)
Rule('catalyze_XIAPC3A_to_XIAP_C3ub',
     XIAP(bf=1) % C3(bf=1, state='A') >> XIAP(bf=None) + C3(bf=None,
                                                            state='ub'),
     catalyze_XIAPC3A_to_XIAP_C3ub_kc)
Rule('bind_C3A_PARPU_to_C3APARPU',
     C3(bf=None, state='A') + PARP(bf=None, state='U') | C3(bf=1,
                                                            state='A') % PARP(
         bf=1, state='U'), bind_C3A_PARPU_to_C3APARPU_kf,
     bind_C3A_PARPU_to_C3APARPU_kr)
Rule('catalyze_C3APARPU_to_C3A_PARPC',
     C3(bf=1, state='A') % PARP(bf=1, state='U') >> C3(bf=None,
                                                       state='A') + PARP(
         bf=None, state='C'), catalyze_C3APARPU_to_C3A_PARPC_kc)
Rule('bind_C3A_C6pro_to_C3AC6pro',
     C3(bf=None, state='A') + C6(bf=None, state='pro') | C3(bf=1,
                                                            state='A') % C6(
         bf=1, state='pro'), bind_C3A_C6pro_to_C3AC6pro_kf,
     bind_C3A_C6pro_to_C3AC6pro_kr)
Rule('catalyze_C3AC6pro_to_C3A_C6A',
     C3(bf=1, state='A') % C6(bf=1, state='pro') >> C3(bf=None,
                                                       state='A') + C6(bf=None,
                                                                       state='A'),
     catalyze_C3AC6pro_to_C3A_C6A_kc)
Rule('bind_C6A_C8pro_to_C6AC8pro',
     C6(bf=None, state='A') + C8(bf=None, state='pro') | C6(bf=1,
                                                            state='A') % C8(
         bf=1, state='pro'), bind_C6A_C8pro_to_C6AC8pro_kf,
     bind_C6A_C8pro_to_C6AC8pro_kr)
Rule('catalyze_C6AC8pro_to_C6A_C8A',
     C6(bf=1, state='A') % C8(bf=1, state='pro') >> C6(bf=None,
                                                       state='A') + C8(bf=None,
                                                                       state='A'),
     catalyze_C6AC8pro_to_C6A_C8A_kc)
Rule('equilibrate_BidT_to_BidM',
     Bid(bf=None, state='T') | Bid(bf=None, state='M'),
     equilibrate_BidT_to_BidM_kf, equilibrate_BidT_to_BidM_kr)
Rule('bind_BidM_BaxC_to_BidMBaxC',
     Bid(bf=None, state='M') + Bax(bf=None, state='C') | Bid(bf=1,
                                                             state='M') % Bax(
         bf=1, state='C'), bind_BidM_BaxC_to_BidMBaxC_kf,
     bind_BidM_BaxC_to_BidMBaxC_kr)
Rule('catalyze_BidMBaxC_to_BidM_BaxM',
     Bid(bf=1, state='M') % Bax(bf=1, state='C') >> Bid(bf=None,
                                                        state='M') + Bax(
         bf=None, state='M'), catalyze_BidMBaxC_to_BidM_BaxM_kc)
Rule('bind_BidM_BaxM_to_BidMBaxM',
     Bid(bf=None, state='M') + Bax(bf=None, state='M') | Bid(bf=1,
                                                             state='M') % Bax(
         bf=1, state='M'), bind_BidM_BaxM_to_BidMBaxM_kf,
     bind_BidM_BaxM_to_BidMBaxM_kr)
Rule('catalyze_BidMBaxM_to_BidM_BaxA',
     Bid(bf=1, state='M') % Bax(bf=1, state='M') >> Bid(bf=None,
                                                        state='M') + Bax(
         bf=None, state='A'), catalyze_BidMBaxM_to_BidM_BaxA_kc)
Rule('bind_BidM_BakM_to_BidMBakM',
     Bid(bf=None, state='M') + Bak(bf=None, state='M') | Bid(bf=1,
                                                             state='M') % Bak(
         bf=1, state='M'), bind_BidM_BakM_to_BidMBakM_kf,
     bind_BidM_BakM_to_BidMBakM_kr)
Rule('catalyze_BidMBakM_to_BidM_BakA',
     Bid(bf=1, state='M') % Bak(bf=1, state='M') >> Bid(bf=None,
                                                        state='M') + Bak(
         bf=None, state='A'), catalyze_BidMBakM_to_BidM_BakA_kc)
Rule('bind_BaxA_BaxM_to_BaxABaxM',
     Bax(bf=None, s1=None, s2=None, state='A') + Bax(bf=None,
                                                     state='M') | Bax(bf=1,
                                                                      s1=None,
                                                                      s2=None,
                                                                      state='A') % Bax(
         bf=1, state='M'), bind_BaxA_BaxM_to_BaxABaxM_kf,
     bind_BaxA_BaxM_to_BaxABaxM_kr)
Rule('catalyze_BaxABaxM_to_BaxA_BaxA',
     Bax(bf=1, s1=None, s2=None, state='A') % Bax(bf=1, state='M') >> Bax(
         bf=None, s1=None, s2=None, state='A') + Bax(bf=None, state='A'),
     catalyze_BaxABaxM_to_BaxA_BaxA_kc)
Rule('bind_BakA_BakM_to_BakABakM',
     Bak(bf=None, s1=None, s2=None, state='A') + Bak(bf=None,
                                                     state='M') | Bak(bf=1,
                                                                      s1=None,
                                                                      s2=None,
                                                                      state='A') % Bak(
         bf=1, state='M'), bind_BakA_BakM_to_BakABakM_kf,
     bind_BakA_BakM_to_BakABakM_kr)
Rule('catalyze_BakABakM_to_BakA_BakA',
     Bak(bf=1, s1=None, s2=None, state='A') % Bak(bf=1, state='M') >> Bak(
         bf=None, s1=None, s2=None, state='A') + Bak(bf=None, state='A'),
     catalyze_BakABakM_to_BakA_BakA_kc)
Rule('bind_BidM_Bcl2M',
     Bid(bf=None, state='M') + Bcl2(bf=None, state='M') | Bid(bf=1,
                                                              state='M') % Bcl2(
         bf=1, state='M'), bind_BidM_Bcl2M_kf, bind_BidM_Bcl2M_kr)
Rule('bind_BidM_BclxLM',
     Bid(bf=None, state='M') + BclxL(bf=None, state='M') | Bid(bf=1,
                                                               state='M') % BclxL(
         bf=1, state='M'), bind_BidM_BclxLM_kf, bind_BidM_BclxLM_kr)
Rule('bind_BidM_Mcl1M',
     Bid(bf=None, state='M') + Mcl1(bf=None, state='M') | Bid(bf=1,
                                                              state='M') % Mcl1(
         bf=1, state='M'), bind_BidM_Mcl1M_kf, bind_BidM_Mcl1M_kr)
Rule('bind_BaxA_Bcl2',
     Bax(bf=None, s1=None, s2=None, state='A') + Bcl2(bf=None) | Bax(bf=1,
                                                                     s1=None,
                                                                     s2=None,
                                                                     state='A') % Bcl2(
         bf=1), bind_BaxA_Bcl2_kf, bind_BaxA_Bcl2_kr)
Rule('bind_BaxA_BclxLM',
     Bax(bf=None, s1=None, s2=None, state='A') + BclxL(bf=None,
                                                       state='M') | Bax(bf=1,
                                                                        s1=None,
                                                                        s2=None,
                                                                        state='A') % BclxL(
         bf=1, state='M'), bind_BaxA_BclxLM_kf, bind_BaxA_BclxLM_kr)
Rule('bind_BakA_BclxLM',
     Bak(bf=None, s1=None, s2=None, state='A') + BclxL(bf=None,
                                                       state='M') | Bak(bf=1,
                                                                        s1=None,
                                                                        s2=None,
                                                                        state='A') % BclxL(
         bf=1, state='M'), bind_BakA_BclxLM_kf, bind_BakA_BclxLM_kr)
Rule('bind_BakA_Mcl1M',
     Bak(bf=None, s1=None, s2=None, state='A') + Mcl1(bf=None,
                                                      state='M') | Bak(bf=1,
                                                                       s1=None,
                                                                       s2=None,
                                                                       state='A') % Mcl1(
         bf=1, state='M'), bind_BakA_Mcl1M_kf, bind_BakA_Mcl1M_kr)
Rule('bind_BadM_Bcl2M',
     Bad(bf=None, state='M') + Bcl2(bf=None, state='M') | Bad(bf=1,
                                                              state='M') % Bcl2(
         bf=1, state='M'), bind_BadM_Bcl2M_kf, bind_BadM_Bcl2M_kr)
Rule('bind_BadM_BclxLM',
     Bad(bf=None, state='M') + BclxL(bf=None, state='M') | Bad(bf=1,
                                                               state='M') % BclxL(
         bf=1, state='M'), bind_BadM_BclxLM_kf, bind_BadM_BclxLM_kr)
Rule('bind_NoxaM_Mcl1M',
     Noxa(bf=None, state='M') + Mcl1(bf=None, state='M') | Noxa(bf=1,
                                                                state='M') % Mcl1(
         bf=1, state='M'), bind_NoxaM_Mcl1M_kf, bind_NoxaM_Mcl1M_kr)
Rule('assemble_pore_sequential_Bax_2',
     Bax(bf=None, s1=None, s2=None, state='A') + Bax(bf=None, s1=None, s2=None,
                                                     state='A') | Bax(bf=None,
                                                                      s1=None,
                                                                      s2=1,
                                                                      state='A') % Bax(
         bf=None, s1=1, s2=None, state='A'), assemble_pore_sequential_Bax_2_kf,
     assemble_pore_sequential_Bax_2_kr)
Rule('assemble_pore_sequential_Bax_3',
     Bax(bf=None, s1=None, s2=None, state='A') + Bax(bf=None, s1=None, s2=1,
                                                     state='A') % Bax(bf=None,
                                                                      s1=1,
                                                                      s2=None,
                                                                      state='A') | MatchOnce(
         Bax(bf=None, s1=3, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                                   state='A') % Bax(bf=None,
                                                                    s1=2, s2=3,
                                                                    state='A')),
     assemble_pore_sequential_Bax_3_kf, assemble_pore_sequential_Bax_3_kr)
Rule('assemble_pore_sequential_Bax_4',
     Bax(bf=None, s1=None, s2=None, state='A') + MatchOnce(
         Bax(bf=None, s1=3, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                                   state='A') % Bax(bf=None,
                                                                    s1=2, s2=3,
                                                                    state='A')) | MatchOnce(
         Bax(bf=None, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                                   state='A') % Bax(bf=None,
                                                                    s1=2, s2=3,
                                                                    state='A') % Bax(
             bf=None, s1=3, s2=4, state='A')),
     assemble_pore_sequential_Bax_4_kf, assemble_pore_sequential_Bax_4_kr)
Rule('assemble_pore_sequential_Bak_2',
     Bak(bf=None, s1=None, s2=None, state='A') + Bak(bf=None, s1=None, s2=None,
                                                     state='A') | Bak(bf=None,
                                                                      s1=None,
                                                                      s2=1,
                                                                      state='A') % Bak(
         bf=None, s1=1, s2=None, state='A'), assemble_pore_sequential_Bak_2_kf,
     assemble_pore_sequential_Bak_2_kr)
Rule('assemble_pore_sequential_Bak_3',
     Bak(bf=None, s1=None, s2=None, state='A') + Bak(bf=None, s1=None, s2=1,
                                                     state='A') % Bak(bf=None,
                                                                      s1=1,
                                                                      s2=None,
                                                                      state='A') | MatchOnce(
         Bak(bf=None, s1=3, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                                   state='A') % Bak(bf=None,
                                                                    s1=2, s2=3,
                                                                    state='A')),
     assemble_pore_sequential_Bak_3_kf, assemble_pore_sequential_Bak_3_kr)
Rule('assemble_pore_sequential_Bak_4',
     Bak(bf=None, s1=None, s2=None, state='A') + MatchOnce(
         Bak(bf=None, s1=3, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                                   state='A') % Bak(bf=None,
                                                                    s1=2, s2=3,
                                                                    state='A')) | MatchOnce(
         Bak(bf=None, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                                   state='A') % Bak(bf=None,
                                                                    s1=2, s2=3,
                                                                    state='A') % Bak(
             bf=None, s1=3, s2=4, state='A')),
     assemble_pore_sequential_Bak_4_kf, assemble_pore_sequential_Bak_4_kr)
Rule('pore_transport_complex_BaxA_4_CytoCM', MatchOnce(
    Bax(bf=None, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                              state='A') % Bax(bf=None, s1=2,
                                                               s2=3,
                                                               state='A') % Bax(
        bf=None, s1=3, s2=4, state='A')) + CytoC(bf=None,
                                                 state='M') | MatchOnce(
    Bax(bf=5, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                           state='A') % Bax(bf=None, s1=2,
                                                            s2=3,
                                                            state='A') % Bax(
        bf=None, s1=3, s2=4, state='A') % CytoC(bf=5, state='M')),
     pore_transport_complex_BaxA_4_CytoCM_kf,
     pore_transport_complex_BaxA_4_CytoCM_kr)
Rule('pore_transport_dissociate_BaxA_4_CytoCC', MatchOnce(
    Bax(bf=5, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                           state='A') % Bax(bf=None, s1=2,
                                                            s2=3,
                                                            state='A') % Bax(
        bf=None, s1=3, s2=4, state='A') % CytoC(bf=5, state='M')) >> MatchOnce(
    Bax(bf=None, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                              state='A') % Bax(bf=None, s1=2,
                                                               s2=3,
                                                               state='A') % Bax(
        bf=None, s1=3, s2=4, state='A')) + CytoC(bf=None, state='C'),
     pore_transport_dissociate_BaxA_4_CytoCC_kc)
Rule('pore_transport_complex_BaxA_4_SmacM', MatchOnce(
    Bax(bf=None, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                              state='A') % Bax(bf=None, s1=2,
                                                               s2=3,
                                                               state='A') % Bax(
        bf=None, s1=3, s2=4, state='A')) + Smac(bf=None,
                                                state='M') | MatchOnce(
    Bax(bf=5, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                           state='A') % Bax(bf=None, s1=2,
                                                            s2=3,
                                                            state='A') % Bax(
        bf=None, s1=3, s2=4, state='A') % Smac(bf=5, state='M')),
     pore_transport_complex_BaxA_4_SmacM_kf,
     pore_transport_complex_BaxA_4_SmacM_kr)
Rule('pore_transport_dissociate_BaxA_4_SmacC', MatchOnce(
    Bax(bf=5, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                           state='A') % Bax(bf=None, s1=2,
                                                            s2=3,
                                                            state='A') % Bax(
        bf=None, s1=3, s2=4, state='A') % Smac(bf=5, state='M')) >> MatchOnce(
    Bax(bf=None, s1=4, s2=1, state='A') % Bax(bf=None, s1=1, s2=2,
                                              state='A') % Bax(bf=None, s1=2,
                                                               s2=3,
                                                               state='A') % Bax(
        bf=None, s1=3, s2=4, state='A')) + Smac(bf=None, state='C'),
     pore_transport_dissociate_BaxA_4_SmacC_kc)
Rule('pore_transport_complex_BakA_4_CytoCM', MatchOnce(
    Bak(bf=None, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                              state='A') % Bak(bf=None, s1=2,
                                                               s2=3,
                                                               state='A') % Bak(
        bf=None, s1=3, s2=4, state='A')) + CytoC(bf=None,
                                                 state='M') | MatchOnce(
    Bak(bf=5, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                           state='A') % Bak(bf=None, s1=2,
                                                            s2=3,
                                                            state='A') % Bak(
        bf=None, s1=3, s2=4, state='A') % CytoC(bf=5, state='M')),
     pore_transport_complex_BakA_4_CytoCM_kf,
     pore_transport_complex_BakA_4_CytoCM_kr)
Rule('pore_transport_dissociate_BakA_4_CytoCC', MatchOnce(
    Bak(bf=5, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                           state='A') % Bak(bf=None, s1=2,
                                                            s2=3,
                                                            state='A') % Bak(
        bf=None, s1=3, s2=4, state='A') % CytoC(bf=5, state='M')) >> MatchOnce(
    Bak(bf=None, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                              state='A') % Bak(bf=None, s1=2,
                                                               s2=3,
                                                               state='A') % Bak(
        bf=None, s1=3, s2=4, state='A')) + CytoC(bf=None, state='C'),
     pore_transport_dissociate_BakA_4_CytoCC_kc)
Rule('pore_transport_complex_BakA_4_SmacM', MatchOnce(
    Bak(bf=None, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                              state='A') % Bak(bf=None, s1=2,
                                                               s2=3,
                                                               state='A') % Bak(
        bf=None, s1=3, s2=4, state='A')) + Smac(bf=None,
                                                state='M') | MatchOnce(
    Bak(bf=5, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                           state='A') % Bak(bf=None, s1=2,
                                                            s2=3,
                                                            state='A') % Bak(
        bf=None, s1=3, s2=4, state='A') % Smac(bf=5, state='M')),
     pore_transport_complex_BakA_4_SmacM_kf,
     pore_transport_complex_BakA_4_SmacM_kr)
Rule('pore_transport_dissociate_BakA_4_SmacC', MatchOnce(
    Bak(bf=5, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                           state='A') % Bak(bf=None, s1=2,
                                                            s2=3,
                                                            state='A') % Bak(
        bf=None, s1=3, s2=4, state='A') % Smac(bf=5, state='M')) >> MatchOnce(
    Bak(bf=None, s1=4, s2=1, state='A') % Bak(bf=None, s1=1, s2=2,
                                              state='A') % Bak(bf=None, s1=2,
                                                               s2=3,
                                                               state='A') % Bak(
        bf=None, s1=3, s2=4, state='A')) + Smac(bf=None, state='C'),
     pore_transport_dissociate_BakA_4_SmacC_kc)

Initial(L(bf=None), L_0)
Initial(R(bf=None), R_0)
Initial(flip(bf=None), Flip_0)
Initial(C8(bf=None, state='pro'), C8_0)
Initial(BAR(bf=None), BAR_0)
Initial(Apaf(bf=None, state='I'), Apaf_0)
Initial(C3(bf=None, state='pro'), C3_0)
Initial(C6(bf=None, state='pro'), C6_0)
Initial(C9(bf=None), C9_0)
Initial(PARP(bf=None, state='U'), PARP_0)
Initial(XIAP(bf=None), XIAP_0)
Initial(Bid(bf=None, state='U'), Bid_0)
Initial(Bax(bf=None, s1=None, s2=None, state='C'), Bax_0)
Initial(Bak(bf=None, s1=None, s2=None, state='M'), Bak_0)
Initial(Bcl2(bf=None, state='M'), Bcl2_0)
Initial(BclxL(bf=None, state='M'), BclxL_0)
Initial(Mcl1(bf=None, state='M'), Mcl1_0)
Initial(Bad(bf=None, state='M'), Bad_0)
Initial(Noxa(bf=None, state='M'), Noxa_0)
Initial(CytoC(bf=None, state='M'), CytoC_0)
Initial(Smac(bf=None, state='M'), Smac_0)

Annotation(L, 'http://identifiers.org/uniprot/P50591', 'is')
Annotation(R, 'http://identifiers.org/uniprot/O14763', 'is')
Annotation(DISC, 'http://identifiers.org/obo.go/GO:0031264', 'is')
Annotation(flip, 'http://identifiers.org/uniprot/O15519', 'is')
Annotation(C8, 'http://identifiers.org/uniprot/Q14790', 'is')
Annotation(BAR, 'http://identifiers.org/uniprot/Q9NZS9', 'is')
Annotation(Bid, 'http://identifiers.org/uniprot/P55957', 'is')
Annotation(Bax, 'http://identifiers.org/uniprot/Q07812', 'is')
Annotation(Bak, 'http://identifiers.org/uniprot/Q16611', 'is')
Annotation(Bcl2, 'http://identifiers.org/uniprot/P10415', 'is')
Annotation(BclxL, 'http://identifiers.org/uniprot/Q07817', 'is')
Annotation(Mcl1, 'http://identifiers.org/uniprot/Q07820', 'is')
Annotation(Bad, 'http://identifiers.org/uniprot/Q92934', 'is')
Annotation(Noxa, 'http://identifiers.org/uniprot/Q13794', 'is')
Annotation(CytoC, 'http://identifiers.org/uniprot/P99999', 'is')
Annotation(Smac, 'http://identifiers.org/uniprot/Q9NR28', 'is')
Annotation(Apaf, 'http://identifiers.org/uniprot/O14727', 'is')
Annotation(Apop, 'http://identifiers.org/obo.go/GO:0043293', 'is')
Annotation(C3, 'http://identifiers.org/uniprot/P42574', 'is')
Annotation(C6, 'http://identifiers.org/uniprot/P55212', 'is')
Annotation(C9, 'http://identifiers.org/uniprot/P55211', 'is')
Annotation(PARP, 'http://identifiers.org/uniprot/P09874', 'is')
Annotation(XIAP, 'http://identifiers.org/uniprot/P98170', 'is')
