SELECT
    CD_REGIAO AS cod_regiao_ibge,
    NM_REGIAO AS nome_regiao_ibge,
    SIGLA_RG AS sigla_regiao_ibge,
    CD_UF AS cod_uf_ibge,
    NM_UF AS nome_uf_ibge,
    SIGLA_UF AS sigla_uf_ibge,
    CD_RGINT AS cod_regiao_interna,
    NM_RGINT AS nome_regiao_interna,
    CAST(AREA_KM2 AS FLOAT) AS area_km2,
    CD_MUN AS cod_municipio_ibge,
    NM_MUN AS nome_municipio_ibge
FROM {{ source('bronze','br_ibge_municipio') }}