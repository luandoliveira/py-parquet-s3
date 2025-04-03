QUERIES = {
    "atividade_coletiva": """
        SELECT 
            tfac.co_seq_fat_atividade_coletiva,
            tfac.co_dim_tempo,
            tfac.ds_outra_localidade, 
            tdt.dt_registro,
            tdp.no_profissional,
            tdc.no_cbo,
            tdus.no_bairro,
            tdus.no_unidade_saude,
            tdt2.ds_turno,
            tfac.nu_participantes,
            tfac.nu_participantes_registrados
        FROM tb_fat_atividade_coletiva tfac 
        JOIN tb_dim_tempo tdt ON tdt.co_seq_dim_tempo = tfac.co_dim_tempo
        JOIN tb_dim_profissional tdp ON tdp.co_seq_dim_profissional = tfac.co_dim_profissional
        JOIN tb_dim_cbo tdc ON tdc.co_seq_dim_cbo = tfac.co_dim_cbo
        JOIN tb_dim_unidade_saude tdus ON tdus.co_seq_dim_unidade_saude = tfac.co_dim_unidade_saude 
        JOIN tb_dim_turno tdt2 ON tdt2.co_seq_dim_turno = tfac.co_dim_turno
    """,

    "atendimento_domiciliar": """
        SELECT 
            tfad.co_seq_fat_atend_domiciliar,
            tfad.co_fat_cidadao_pec,
            tdt.dt_registro,
            tdt2.ds_turno,
            tdp.no_profissional,
            tdc.no_cbo,
            tdus.no_unidade_saude,
            tdus.no_bairro,
            tdfe.ds_faixa_etaria,
            tds.ds_sexo
        FROM tb_fat_atendimento_domiciliar tfad 
        JOIN tb_dim_tempo tdt ON tdt.co_seq_dim_tempo = tfad.co_dim_tempo
        JOIN tb_dim_turno tdt2 ON tdt2.co_seq_dim_turno = tfad.co_dim_turno
        JOIN tb_dim_profissional tdp ON tdp.co_seq_dim_profissional = tfad.co_dim_profissional_1 
        JOIN tb_dim_cbo tdc ON tdc.co_seq_dim_cbo = tfad.co_dim_cbo_1 
        JOIN tb_dim_unidade_saude tdus ON tdus.co_seq_dim_unidade_saude = tfad.co_dim_unidade_saude_1 
        JOIN tb_dim_faixa_etaria tdfe ON tdfe.co_seq_dim_faixa_etaria = tfad.co_dim_faixa_etaria
        JOIN tb_dim_sexo tds ON tds.co_seq_dim_sexo = tfad.co_dim_sexo
    """,

    "atendimento_individual": """
        SELECT 
            tfai.co_seq_fat_atd_ind, 
            tfai.co_fat_cidadao_pec,
            tdfe.ds_faixa_etaria,
            tds.ds_sexo,
            tfai.co_dim_tempo, 
            tdt.dt_registro,
            tdp.nu_cns,
            tdp.no_profissional,
            tdc.no_cbo,
            tfai.co_dim_unidade_saude_1,
            tdus.no_unidade_saude,
            tdus.no_bairro,
            tdta2.ds_tipo_atendimento, 
            tdt2.ds_turno,
            tdla.ds_local_atendimento
        FROM tb_fat_atendimento_individual tfai 
        JOIN tb_dim_tempo tdt ON tdt.co_seq_dim_tempo = tfai.co_dim_tempo
        JOIN tb_dim_profissional tdp ON tdp.co_seq_dim_profissional = tfai.co_dim_profissional_1 
        JOIN tb_dim_cbo tdc ON tdc.co_seq_dim_cbo = tfai.co_dim_cbo_1
        JOIN tb_dim_unidade_saude tdus ON tdus.co_seq_dim_unidade_saude = tfai.co_dim_unidade_saude_1 
        JOIN tb_dim_tipo_atendimento tdta2 ON tdta2.co_seq_dim_tipo_atendimento = tfai.co_dim_tipo_atendimento 
        JOIN tb_dim_turno tdt2 ON tdt2.co_seq_dim_turno = tfai.co_dim_turno
        JOIN tb_dim_faixa_etaria tdfe ON tdfe.co_seq_dim_faixa_etaria = tfai.co_dim_faixa_etaria
        JOIN tb_dim_sexo tds ON tds.co_seq_dim_sexo = tfai.co_dim_sexo
        JOIN tb_dim_local_atendimento tdla ON tdla.co_seq_dim_local_atendimento = tfai.co_dim_local_atendimento
    """,

    "atendimento_odontologico": """
    select 
        od.co_seq_fat_atd_odnt, 
        od.co_fat_cidadao_pec, 
        od.co_dim_tempo,
        tdt.co_seq_dim_tempo,
        tdt.dt_registro,
        od.dt_inicial_atendimento, 
        od.co_dim_unidade_saude_1,
        tdus.no_unidade_saude,
        tdus.no_bairro, 
        od.st_paciente_necessidades_espec,
        od.st_gestante,
        od.st_vigil_abscesso_dentoalveola,
        od.st_vigil_alterac_tecidos_moles,
        od.st_vigil_dor_dente,
        od.st_vigil_fendas_fissuras_labio,
        od.st_vigil_fluorose_dentaria,
        od.st_vigil_traumat_dentoalveolar,
        od.st_vigil_nao_identificado,
        od.st_fornecimento_escova_dental,
        od.st_fornecimento_creme_dental,
        od.st_fornecimento_fio_dental,
        od.st_conduta_consulta_agendada,
        od.st_conduta_outros_profissio_ab,
        tdp.nu_cns,
        tdp.no_profissional,
        tdtco.ds_tipo_consulta_odonto,
        tdta.nu_identificador,
        tdta.ds_tipo_atendimento,
        tdt2.ds_turno,
        tdfe.ds_faixa_etaria,
        tds.ds_sexo,
        tdc.ds_filtro,
        tdc.no_cbo
    from tb_fat_atendimento_odonto od
    join tb_dim_tempo tdt on tdt.co_seq_dim_tempo = od.co_dim_tempo
    join tb_dim_unidade_saude tdus on tdus.co_seq_dim_unidade_saude = od.co_dim_unidade_saude_1 
    join tb_dim_profissional tdp on tdp.co_seq_dim_profissional = od.co_dim_profissional_1 
    join tb_dim_tipo_consulta_odonto tdtco on tdtco.co_seq_dim_tipo_cnsulta_odonto = od.co_dim_tipo_consulta
    join tb_dim_tipo_atendimento tdta on tdta.co_seq_dim_tipo_atendimento = od.co_dim_tipo_atendimento
    join tb_dim_turno tdt2 on tdt2.co_seq_dim_turno = od.co_dim_turno
    join tb_dim_faixa_etaria tdfe  on tdfe.co_seq_dim_faixa_etaria = od.co_dim_faixa_etaria
    join tb_dim_sexo tds  on tds.co_seq_dim_sexo = od.co_dim_sexo
    join tb_dim_cbo tdc  on tdc.co_seq_dim_cbo = od.co_dim_cbo_1
"""
}