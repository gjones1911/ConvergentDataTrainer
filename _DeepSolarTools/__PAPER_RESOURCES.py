from _DeepSolarTools.__DEEPSOLAR_Resources import state_abrev
import numpy as np

HMcvr_dic = {
"DS_HighSolar":"DS_HSLR",
"High_Solar_Areas":"HSLR",
"Hot_Spots_AvgAr":"HS_avgA",
"Hot_Spots_hh":"HS_hh",
"Hot_Spots_hown":"HS_hown",
"Income_x_EnergyCost":"IncEcst",
"Low_Solar_Areas":"LSLR",
"Mid West":"MWest",
"NorthEast":"NEast",
"Policy_Combo":"Pol_Cmb",
"Savings_potential":"Svg_Pot",
"South":"South",
"Tot_own_mw":"TtOwnMw",
"URBAN":"Urban",
"West":"West",
"Yr_own_mwh":"YrGenMWH",
"Yrl_%_inc":"YrPtInc",
"asian_pct":"AsianRt",
"average_household_size":"AvgSzHH",
"avg_monthly_consumption_kwh":"AvConsm",
"black_pct":"BlackRt",
"cdd":"cdd",
"cdd_std":"cdd_std",
"climate_zone":"climZn",
"daily_solar_radiation":"DlySlr",
"diversity":"Divrsty",
"dlrs_kwh":"dlrskwh",
"educated_population_rate":"EduPopRt",
"education_bachelor_or_above_rate":"EduBsP",
"education_bachelor_rate":"EduBsRt",
"education_college_rate":"EduClRt",
"education_doctoral_rate":"EduDrRt",
"female_pct":"FemaleRt",
"hh_gini_index":"IncGini",
"high_own_elep_hh":"H_elp",
"hispanic_pct":"HispRt",
"household_count":"HH_cnt",
"household_type_family_rate":"FamRt",
"hu_2000toafter_pct":"Newer_H",
"hu_med_val":"MedHVal",
"hu_own_pct":"HownRt",
"locale_recode(rural)":"Rural",
"locale_recode(suburban)":"Suburb",
"low_own_elep_hh":"L_elp",
"lowincome_tax_credit_bin":"LI_TC_b",
"median_household_income":"MedHInc",
"mod_own_elep_hh":"Md_elp",
"net_metering_bin":"Net_Met",
"number_of_solar_system_per_household":"PvPerHH",
"ownership_x_TotOK_Rcnt":"OwnTtRc",
"ownership_x_TotOK_Rm2":"OwnTtM2",
"ownership_x_TotOK_cnt":"OwnTtCt",
"pop25_some_college_plus":"Edu25_Cl",
"pop_med_age":"MedAge",
"popden_x_TotOK_RCnt":"PdnTtRCt",
"popden_x_TotOK_Rm2":"PdnTtRM2",
"popden_x_TotOK_cnt":"PdnTt_Ct",
"population_density":"PopDen",
"property_tax_bin":"Pr_Tax",
"rural_diversity":"R_div",
"solar_prod":"SlrPrd",
"suburban_diversity":"Su_div",
"total_own_Sbldg":"Tt_Sbld",
"total_own_devp":"Tt_devp",
"total_own_devpC":"Tt_devC",
"total_own_elep":"TtElep",
"total_own_hh":"Tt_o_hh",
"travel_time_10_19_rate":"Com_10_19",
"travel_time_20_39_rate":"Com_20_39",
"travel_time_40_89_rate":"Com_40_89",
"travel_time_average":"",
"travel_time_less_than_10_rate":"",
"urban_diversity":"UrbanDv",
"verylow_own_elep_hh":"VL_elp",
}

cvr_dicT = {
"DS_HighSolar":"DS_HighSolar",
"High_Solar_Areas":"High_Solar_Areas",
"Hot_Spots_AvgAr":"Hot_Spots_AvgAr",
"Hot_Spots_hh":"Hot_Spots_hh",
"Hot_Spots_hown":"Hot_Spots_hown",
"Income_x_EnergyCost":"Income_x_EnergyCost",
"Low_Solar_Areas":"Low_Solar_Areas",
"Mid West":"Mid_West",
"NorthEast":"NorthEast",
"Policy_Combo":"Policy_Combo",
"Savings_potential":"Savings_potential",
"South":"South",
"Tot_own_mw":"Total_owned_capcity",
"URBAN":"Urban",
"West":"West",
"Yr_own_mwh":"Annual_Gen_Potential",
"Yrl_%_inc":"Annual_Income_pct_saved",
"asian_pct":"Asian_pct",
"average_household_size":"Average_number_in_home",
"avg_monthly_consumption_kwh":"Avg_monthly_consumption_kwh",
"black_pct":"Black_pct",
"ca":"ca",
"cdd":"cdd",
"cdd_std":"cdd_std",
"climate_zone":"Climate_zone",
"daily_solar_radiation":"Daily_solar_radiation",
"diversity":"Diversity",
"dlrs_kwh":"Energy_cost",
"educated_population_rate":"Educated_population_rate",
"education_bachelor_or_above_rate":"Education_bachelor_or_above_rate",
"education_bachelor_rate":"Education_bachelor_rate",
"education_college_rate":"Education_college_rate",
"education_doctoral_rate":"Education_doctoral_rate",
"female_pct":"Female_pct",
"hh_gini_index":"hh_gini_index",
"high_own_elep_hh":"high_own_elep_hh",
"hispanic_pct":"hispanic_pct",
"household_count":"household_count",
"household_type_family_rate":"household_type_family_rate",
"hu_2000toafter_pct":"Homes_built_after_1999_rt",
"hu_med_val":"hu_med_val",
"hu_own_pct":"hu_own_pct",
"locale_recode(rural)":"Rural",
"locale_recode(suburban)":"Suburban",
"low_own_elep_hh":"low_own_elep_hh",
"lowincome_tax_credit_bin":"lowincome_tax_credit_bin",
"median_household_income":"Median_income",
"mod_own_elep_hh":"mod_own_elep_hh",
"net_metering_bin":"net_metering_bin",
"number_of_solar_system_per_household":"number_of_solar_system_per_household",
"ownership_x_TotOK_Rcnt":"ownership_x_TotOK_Rcnt",
"ownership_x_TotOK_Rm2":"ownership_x_TotOK_Rm2",
"ownership_x_TotOK_cnt":"ownership_x_TotOK_cnt",
"pop25_some_college_plus":"pop25_some_college_plus",
"pop_med_age":"pop_med_age",
"popden_x_TotOK_RCnt":"popden_x_TotOK_RCnt",
"popden_x_TotOK_Rm2":"popden_x_TotOK_Rm2",
"popden_x_TotOK_cnt":"popden_x_TotOK_cnt",
"population_density":"population_density",
"property_tax_bin":"property_tax_bin",
"rural_diversity":"rural_diversity",
"solar_prod":"solar_prod",
"suburban_diversity":"suburban_diversity",
"total_own_Sbldg":"total_own_Sbldg",
"total_own_devp":"total_own_devp",
"total_own_devpC":"total_own_devpC",
"total_own_elep":"total_own_elep",
"total_own_hh":"total_own_hh",
"travel_time_10_19_rate":"travel_time_10_19_rate",
"travel_time_20_39_rate":"travel_time_20_39_rate",
"travel_time_40_89_rate":"travel_time_40_89_rate",
"travel_time_average":"travel_time_average",
"travel_time_less_than_10_rate":"travel_time_less_than_10_rate",
"urban_diversity":"urban_diversity",
"verylow_own_elep_hh":"verylow_own_elep_hh",
}



behavior_v = [
    "travel_time_10_19_rate",
    "travel_time_20_29_rate",
    "travel_time_30_39_rate",
    'travel_time_20_39_rate',
    "travel_time_40_89_rate",
    "travel_time_average",
    "travel_time_less_than_10_rate",
'avg_monthly_consumption_kwh',
]

behavior_vp = [
    #"travel_time_10_19_rate",
    #"travel_time_20_29_rate",
    #"travel_time_30_39_rate",
    #'travel_time_20_39_rate',
    "travel_time_40_89_rate",
    #"travel_time_average",
    #"travel_time_less_than_10_rate",
    'avg_monthly_consumption_kwh',
]


behavior_vT = [
    "travel_time_10_19_rate",
    #"travel_time_20_29_rate",
    #"travel_time_30_39_rate",
    'travel_time_20_39_rate',
    "travel_time_40_89_rate",
    "travel_time_average",
    "travel_time_less_than_10_rate",
'avg_monthly_consumption_kwh',
]


policy_fin = [
    'lowincome_tax_credit_bin',
    "net_metering_bin",
    "property_tax_bin",
    'dlrs_kwh',
    'Policy_Combo',
    
    "total_own_elep",
    "high_own_elep_hh",
    #"high_mf_own_elep_hh",
    #"high_sf_own_elep_hh",
    #"low_mf_own_elep_hh",
    "low_own_elep_hh",
    #"low_sf_own_elep_hh",
    #"mod_mf_own_elep_hh",
    "mod_own_elep_hh",
    #"mod_sf_own_elep_hh",
    #"very_low_mf_own_elep_hh",
    "verylow_own_elep_hh",
    "Yrl_%_inc",
]

policy_finp = [
    #'lowincome_tax_credit_bin',
    "net_metering_bin",
    "property_tax_bin",
    'dlrs_kwh',
    #'Policy_Combo',

    #"total_own_elep",
    #"high_own_elep_hh",
    # "high_mf_own_elep_hh",
    # "high_sf_own_elep_hh",
    # "low_mf_own_elep_hh",
    #"low_own_elep_hh",
    # "low_sf_own_elep_hh",
    # "mod_mf_own_elep_hh",
    #"mod_own_elep_hh",
    # "mod_sf_own_elep_hh",
    # "very_low_mf_own_elep_hh",
    #"verylow_own_elep_hh",
    # "Yrl_%_inc",
]


personals_vars = [
    "female_pct",
    "male_pct",
    "hispanic_pct",
    "asian_pct",
    "black_pct",
    "diversity",

    "pop_med_age",

    "pop_over_65",
    "pop_total",
    "pop_under_18",
    "pop_us_citizen",
    "population",
    "population_density",
    'urban_diversity',
    'rural_diversity',
    'suburban_diversity',
    'popden_x_TotOK_cnt',
    'popden_x_TotOK_RCnt',
    'popden_x_TotOK_Rm2',

]

PerVarB = [
    'pop_female',
    'pop_male',
    "female_pct",
    "male_pct",
    'Gender_Ratio',
    "hispanic_pct",
    "asian_pct",
    "black_pct",
    "white_pct",
    "diversity",

    "pop_med_age",

    #"pop_over_65",
    #"pop_total",
    #"pop_under_18",
    #"pop_us_citizen",
    #"population",
    "population_density",
    'urban_diversity',
    'rural_diversity',
    'suburban_diversity',
    'popden_x_TotOK_cnt',
    'popden_x_TotOK_RCnt',
    'popden_x_TotOK_Rm2',
    "educated_population_rate",
    "education_bachelor_or_above_rate",
    "education_bachelor_rate",
    "education_college_rate",
    "education_doctoral_rate",
    "pop25_some_college_plus",
]


Financial_resources = [
    "household_type_family_rate",
    'average_household_size',
    "pct_eli_hh",

    "hh_gini_index",
    'median_household_income',
    "housing_unit_median_value",

    "hh_size_1",
    "hh_size_2",
    "hh_size_3",
    "hh_size_4",
    "hh_total",

    "high_hh_rate",
    "high_own_hh",
    "high_mf_own_hh",
    "high_sf_own_hh",

    "low_hh_rate",
    "low_mf_own_hh",
    "low_own_hh",
    "low_sf_own_hh",

    "very_low_hh_rate",
    "very_low_mf_own_hh",
    "verylow_own_hh",
    "very_low_sf_own_hh",

    "mid_hh_rate",
    "mid_mf_own_hh",
    "mid_own_hh",
    "mid_sf_own_hh",

    "mod_hh_rate",
    "mod_mf_own_hh",
    "mod_sf_own_hh",
    "mod_own_hh",

    "total_mf_own_hh",

    "hu_monthly_owner_costs_greaterthan_1000dlrs",
    "hu_monthly_owner_costs_lessthan_1000dlrs",

    "occ_rate",
    'hu_own_pct',
    'ownership_x_TotOK_cnt',
    'ownership_x_TotOK_Rcnt',
    'ownership_x_TotOK_Rm2',

    "dlrs_kwh x median_household_income",
    'Inc_x_Consmpt_kwh',
    "employ_rate",

    "fam_children_6to17",
    "fam_children_under_6",
    "fam_med_income",
]

occu_vars = [
    "occupation_administrative_rate",
    "occupation_agriculture_rate",
    "occupation_arts_rate",
    "occupation_construction_rate",
    "occupation_education_rate",
    "occupation_finance_rate",
    "occupation_information_rate",
    "occupation_manufacturing_rate",
    "occupation_public_rate",
    "occupation_retail_rate",
    "occupation_transportation_rate",
    "occupation_wholesale_rate",
]

unemploy_vars = [
    "p16_unemployed",
    "pop25_high_school",
    "pop25_no_high_school",
    "pop25_some_college_plus",
    "pop25_some_college_plus_log10",
]

FinReB = [
    "household_type_family_rate",
    'employ_rate',
    "pct_eli_hh",

    "hh_gini_index",
    'median_household_income',
    "occ_rate",
    'hu_own_pct',

    'hu_med_val',

    'average_household_size',
    #'hu_own_pct',
    'occupancy_owner_rate',
]

FinReP = [
    "household_type_family_rate",
    #"pct_eli_hh",
    "hh_gini_index",
    'median_household_income',
    #'Inc_x_Consmpt_kwh',
    #"Income_x_Suitable_m2",
    #"housing_unit_median_value",
    'average_household_size',
    'hu_own_pct',
    'hu_med_val',
    #'occupancy_owner_rate',
]

FinRePp = [
    "household_type_family_rate",
    #"pct_eli_hh",
    #"hh_gini_index",
    'median_household_income',
    #'Inc_x_Consmpt_kwh',
    #"Income_x_Suitable_m2",
    #"housing_unit_median_value",
    'average_household_size',
    'hu_own_pct',
    'hu_med_val',
    #'occupancy_owner_rate',
]

SuitRPVp = [
    #"hdd",
    'daily_solar_radiation',
    "cdd_std",
    #"hdd_std",
    #"cdd",
    #"heating_design_temperature",
    #"cooling_design_temperature",
    #"heating_fuel_housing_unit_count",
    "climate_zone",

    #"household_count",
    #"housing_unit_count",

    #"hu_1959toearlier",
    #"hu_1959toearlier_pct",
    #"hu_1960to1979_pct",
    #"hu_1980to1999_pct",
    #"hu_2000toafter",
    "hu_2000toafter_pct",

    "locale_recode(rural)",
    "locale_recode(suburban)",
    #"locale_recode(town)",
    #"locale_recode(urban)",
    #'URBAN',

    #"solar_prod",

    #"total_own_Sbldg",
    #"total_own_devp",
    #"total_own_devpC",
    #"total_own_hh",
    #"Tot_own_mw",
    #"Yr_own_mwh",
    #"high_own_Sbldg",
    #"high_own_Sbldg_rt",
    #"high_own_devp",
    #"high_own_mwh",

    #"high_mf_own_bldg_cnt",
    #"high_mf_own_devp_cnt",
    #"high_mf_own_devp_m2",
    #"high_mf_own_mw",
    #"high_mf_own_mwh",

    #"high_sf_own_bldg_cnt",
    #"high_sf_own_devp_cnt",
    #"high_sf_own_devp_m2",
    #"high_sf_own_mw",
    #"high_sf_own_mwh",

    #"low_mf_own_bldg_cnt",
    #"low_mf_own_devp_cnt",
    #"low_mf_own_devp_m2",
    #"low_mf_own_mw",
    #"low_mf_own_mwh",

    #"low_own_Sbldg",
    #"low_own_Sbldg_rt",
    #"low_own_devp",
    #"low_own_mwh",

    #"low_sf_own_bldg_cnt",
    #"low_sf_own_devp_cnt",
    #"low_sf_own_devp_m2",
    #"low_sf_own_mw",
    #"low_sf_own_mwh",
    #"mid_mf_own_bldg_cnt",
    #"mid_mf_own_devp_cnt",
    #"mid_mf_own_devp_m2",
    #"mid_mf_own_mw",
    #"mid_mf_own_mwh",

    #"mid_own_Sbldg",
    #"mid_own_Sbldg_rt",
    #"mid_own_devp",
    #"mid_own_mwh",

    #"mid_sf_own_bldg_cnt",
    #"mid_sf_own_devp_cnt",
    #"mid_sf_own_devp_m2",
    #"mid_sf_own_mw",
    #"mid_sf_own_mwh",
    #"mod_mf_own_bldg_cnt",
    #"mod_mf_own_devp_cnt",
    #"mod_mf_own_devp_m2",
    #"mod_mf_own_mw",
    #"mod_mf_own_mwh",

    #"mod_own_Sbldg",
    #"mod_own_Sbldg_rt",
    #"mod_own_devp",
    #"mod_own_mwh",

    #"mod_sf_own_bldg_cnt",
    #"mod_sf_own_devp_cnt",
    #"mod_sf_own_devp_m2",
    #"mod_sf_own_mw",
    #"mod_sf_own_mwh",

    #"very_low_mf_own_bldg_cnt",
    #"very_low_mf_own_devp_cnt",
    #"very_low_mf_own_devp_m2",
    #"very_low_mf_own_mw",
    #"very_low_mf_own_mwh",

    #"verylow_own_Sbldg",
    #"verylow_own_Sbldg_rt",
    #"verylow_own_devp",

    #"very_low_sf_own_bldg_cnt",
    #"very_low_sf_own_devp_cnt",
    #"very_low_sf_own_devp_m2",
    #"very_low_sf_own_mw",
    #"very_low_sf_own_mwh",
]

interactionsp = [
    'ownership_x_TotOK_cnt',
    'ownership_x_TotOK_Rcnt',
    'ownership_x_TotOK_Rm2',
    "Yrl_savings_$",
    'Savings_potential',
    'Income_x_EnergyCost',
    'Inc_x_Consmpt_kwh',
    "Income_x_Suitable_m2",
    'income_x_consumption_energyCost',
    'Income_x_College_Edu',
    'Cost_x_Consumption',
    #'Inc_x_Consmpt_kwh',
    #"Income_x_Suitable_m2",
    #'urban_diversity',
    #'suburban_diversity',
    'rural_diversity',
]

personals_varsp = [
    "female_pct",
    #"male_pct",
    #"hispanic_pct",
    #"asian_pct",
    #"black_pct",
    "diversity",

    "pop_med_age",
    #"pop_over_65",
    #"pop_total",
    #"pop_under_18",
    #"pop_us_citizen",
    #"population",
    "population_density",
    "pop25_some_college_plus",
    #'urban_diversity',
    #'rural_diversity',
    #'suburban_diversity',
    #'popden_x_TotOK_cnt',
    #'popden_x_TotOK_RCnt',
    #'popden_x_TotOK_Rm2',

]

SuitRPV = [
    #"hdd",
    'daily_solar_radiation',
    "cdd",
    #"hdd_std",
    "cdd_std",
    #"heating_design_temperature",
    #"cooling_design_temperature",
    #"heating_fuel_housing_unit_count",
    "climate_zone",

    "household_count",
    #"housing_unit_count",

    #"hu_1959toearlier",
    #"hu_1959toearlier_pct",
    #"hu_1960to1979_pct",
    #"hu_1980to1999_pct",
    #"hu_2000toafter",
    "hu_2000toafter_pct",

    "locale_recode(rural)",
    "locale_recode(suburban)",
    #"locale_recode(town)",
    #"locale_recode(urban)",
    'URBAN',

    "solar_prod",

    "total_own_Sbldg",
    "total_own_devp",
    "total_own_devpC",
    "total_own_hh",
    "Tot_own_mw",
    "Yr_own_mwh",
    #"high_own_Sbldg",
    #"high_own_Sbldg_rt",
    #"high_own_devp",
    #"high_own_mwh",

    #"high_mf_own_bldg_cnt",
    #"high_mf_own_devp_cnt",
    #"high_mf_own_devp_m2",
    #"high_mf_own_mw",
    #"high_mf_own_mwh",

    #"high_sf_own_bldg_cnt",
    #"high_sf_own_devp_cnt",
    #"high_sf_own_devp_m2",
    #"high_sf_own_mw",
    #"high_sf_own_mwh",

    #"low_mf_own_bldg_cnt",
    #"low_mf_own_devp_cnt",
    #"low_mf_own_devp_m2",
    #"low_mf_own_mw",
    #"low_mf_own_mwh",

    #"low_own_Sbldg",
    #"low_own_Sbldg_rt",
    #"low_own_devp",
    #"low_own_mwh",

    #"low_sf_own_bldg_cnt",
    #"low_sf_own_devp_cnt",
    #"low_sf_own_devp_m2",
    #"low_sf_own_mw",
    #"low_sf_own_mwh",
    #"mid_mf_own_bldg_cnt",
    #"mid_mf_own_devp_cnt",
    #"mid_mf_own_devp_m2",
    #"mid_mf_own_mw",
    #"mid_mf_own_mwh",

    #"mid_own_Sbldg",
    #"mid_own_Sbldg_rt",
    #"mid_own_devp",
    #"mid_own_mwh",

    #"mid_sf_own_bldg_cnt",
    #"mid_sf_own_devp_cnt",
    #"mid_sf_own_devp_m2",
    #"mid_sf_own_mw",
    #"mid_sf_own_mwh",
    #"mod_mf_own_bldg_cnt",
    #"mod_mf_own_devp_cnt",
    #"mod_mf_own_devp_m2",
    #"mod_mf_own_mw",
    #"mod_mf_own_mwh",

    #"mod_own_Sbldg",
    #"mod_own_Sbldg_rt",
    #"mod_own_devp",
    #"mod_own_mwh",

    #"mod_sf_own_bldg_cnt",
    #"mod_sf_own_devp_cnt",
    #"mod_sf_own_devp_m2",
    #"mod_sf_own_mw",
    #"mod_sf_own_mwh",

    #"very_low_mf_own_bldg_cnt",
    #"very_low_mf_own_devp_cnt",
    #"very_low_mf_own_devp_m2",
    #"very_low_mf_own_mw",
    #"very_low_mf_own_mwh",

    #"verylow_own_Sbldg",
    #"verylow_own_Sbldg_rt",
    #"verylow_own_devp",

    #"very_low_sf_own_bldg_cnt",
    #"very_low_sf_own_devp_cnt",
    #"very_low_sf_own_devp_m2",
    #"very_low_sf_own_mw",
    #"very_low_sf_own_mwh",
]

SuitRPV2 = [
    #"hdd",
    'daily_solar_radiation',
    "cdd",
    #"hdd_std",
    "cdd_std",
    #"heating_design_temperature",
    #"cooling_design_temperature",
    #"heating_fuel_housing_unit_count",
    "climate_zone",

    "household_count",
    #"housing_unit_count",

    #"hu_1959toearlier",
    #"hu_1959toearlier_pct",
    #"hu_1960to1979_pct",
    #"hu_1980to1999_pct",
    #"hu_2000toafter",
    "hu_2000toafter_pct",

    "locale_recode(rural)",
    "locale_recode(suburban)",
    #"locale_recode(town)",
    #"locale_recode(urban)",
    'URBAN',

    "solar_prod",

    "total_own_Sbldg",
    "total_own_devp",
    "total_own_devpC",
    "total_own_hh",
    "Tot_own_mw",
    "Yr_own_mwh",
    #"high_own_Sbldg",
    #"high_own_Sbldg_rt",
    #"high_own_devp",
    #"high_own_mwh",

    #"high_mf_own_bldg_cnt",
    #"high_mf_own_devp_cnt",
    #"high_mf_own_devp_m2",
    #"high_mf_own_mw",
    #"high_mf_own_mwh",

    #"high_sf_own_bldg_cnt",
    #"high_sf_own_devp_cnt",
    #"high_sf_own_devp_m2",
    #"high_sf_own_mw",
    #"high_sf_own_mwh",

    #"low_mf_own_bldg_cnt",
    #"low_mf_own_devp_cnt",
    #"low_mf_own_devp_m2",
    #"low_mf_own_mw",
    #"low_mf_own_mwh",

    #"low_own_Sbldg",
    #"low_own_Sbldg_rt",
    #"low_own_devp",
    #"low_own_mwh",

    #"low_sf_own_bldg_cnt",
    #"low_sf_own_devp_cnt",
    #"low_sf_own_devp_m2",
    #"low_sf_own_mw",
    #"low_sf_own_mwh",
    #"mid_mf_own_bldg_cnt",
    #"mid_mf_own_devp_cnt",
    #"mid_mf_own_devp_m2",
    #"mid_mf_own_mw",
    #"mid_mf_own_mwh",

    #"mid_own_Sbldg",
    #"mid_own_Sbldg_rt",
    #"mid_own_devp",
    #"mid_own_mwh",

    #"mid_sf_own_bldg_cnt",
    #"mid_sf_own_devp_cnt",
    #"mid_sf_own_devp_m2",
    #"mid_sf_own_mw",
    #"mid_sf_own_mwh",
    #"mod_mf_own_bldg_cnt",
    #"mod_mf_own_devp_cnt",
    #"mod_mf_own_devp_m2",
    #"mod_mf_own_mw",
    #"mod_mf_own_mwh",

    #"mod_own_Sbldg",
    #"mod_own_Sbldg_rt",
    #"mod_own_devp",
    #"mod_own_mwh",

    #"mod_sf_own_bldg_cnt",
    #"mod_sf_own_devp_cnt",
    #"mod_sf_own_devp_m2",
    #"mod_sf_own_mw",
    #"mod_sf_own_mwh",

    #"very_low_mf_own_bldg_cnt",
    #"very_low_mf_own_devp_cnt",
    #"very_low_mf_own_devp_m2",
    #"very_low_mf_own_mw",
    #"very_low_mf_own_mwh",

    #"verylow_own_Sbldg",
    #"verylow_own_Sbldg_rt",
    #"verylow_own_devp",

    #"very_low_sf_own_bldg_cnt",
    #"very_low_sf_own_devp_cnt",
    #"very_low_sf_own_devp_m2",
    #"very_low_sf_own_mw",
    #"very_low_sf_own_mwh",
]
climate_vars = [
    "hdd",
    "cdd",
    "hdd_std",
    "cdd_std",
    "heating_design_temperature",
    "cooling_design_temperature",
    "heating_fuel_housing_unit_count",
    "climate_zone",

    "household_count",
    "housing_unit_count",

    "hu_1959toearlier",
    "hu_1959toearlier_pct",
    "hu_1960to1979_pct",
    "hu_1980to1999_pct",
    "hu_2000toafter",
    "hu_2000toafter_pct",

    "locale_recode(rural)",
    "locale_recode(suburban)",
    "locale_recode(town)",
    "locale_recode(urban)",

    "solar_prod",

    "total_own_Sbldg",
    "total_own_devp",
    "total_own_elep",
    "total_own_hh",

    "high_own_Sbldg",
    "high_own_Sbldg_rt",
    "high_own_devp",
    "high_own_mwh",

    "high_mf_own_bldg_cnt",
    "high_mf_own_devp_cnt",
    "high_mf_own_devp_m2",
    "high_mf_own_mw",
    "high_mf_own_mwh",

    "high_sf_own_bldg_cnt",
    "high_sf_own_devp_cnt",
    "high_sf_own_devp_m2",
    "high_sf_own_mw",
    "high_sf_own_mwh",

    "low_mf_own_bldg_cnt",
    "low_mf_own_devp_cnt",
    "low_mf_own_devp_m2",
    "low_mf_own_mw",
    "low_mf_own_mwh",

    "low_own_Sbldg",
    "low_own_Sbldg_rt",
    "low_own_devp",
    "low_own_mwh",

    "low_sf_own_bldg_cnt",
    "low_sf_own_devp_cnt",
    "low_sf_own_devp_m2",
    "low_sf_own_mw",
    "low_sf_own_mwh",
    "mid_mf_own_bldg_cnt",
    "mid_mf_own_devp_cnt",
    "mid_mf_own_devp_m2",
    "mid_mf_own_mw",
    "mid_mf_own_mwh",

    "mid_own_Sbldg",
    "mid_own_Sbldg_rt",
    "mid_own_devp",
    "mid_own_mwh",

    "mid_sf_own_bldg_cnt",
    "mid_sf_own_devp_cnt",
    "mid_sf_own_devp_m2",
    "mid_sf_own_mw",
    "mid_sf_own_mwh",
    "mod_mf_own_bldg_cnt",
    "mod_mf_own_devp_cnt",
    "mod_mf_own_devp_m2",
    "mod_mf_own_mw",
    "mod_mf_own_mwh",

    "mod_own_Sbldg",
    "mod_own_Sbldg_rt",
    "mod_own_devp",
    "mod_own_mwh",

    "mod_sf_own_bldg_cnt",
    "mod_sf_own_devp_cnt",
    "mod_sf_own_devp_m2",
    "mod_sf_own_mw",
    "mod_sf_own_mwh",

    "very_low_mf_own_bldg_cnt",
    "very_low_mf_own_devp_cnt",
    "very_low_mf_own_devp_m2",
    "very_low_mf_own_mw",
    "very_low_mf_own_mwh",

    "verylow_own_Sbldg",
    "verylow_own_Sbldg_rt",
    "verylow_own_devp",

    "very_low_sf_own_bldg_cnt",
    "very_low_sf_own_devp_cnt",
    "very_low_sf_own_devp_m2",
    "very_low_sf_own_mw",
    "very_low_sf_own_mwh",

    "Tot_own_mw",
    "Yr_own_mwh",
]

edu_vars = [
    "educated_population_rate",
    "education_bachelor_or_above_rate",
    "education_bachelor_rate",
    "education_college_rate",
    "education_doctoral_rate",
    'education_high_school_or_above_rate'
    "education_high_school_graduate_rate",
    "education_high_school_or_below_rate",
    "education_less_than_high_school_rate",
    "education_master_or_above_rate",
    "education_master_rate",
    "education_professional_school_rate",
    # "education_doctoral",
    # "education_high_school_graduate",
    # "education_less_than_high_school",
    # "education_master",
    # "education_population",
    # "education_professional_school",
    # "education_college",
    # "education_bachelor",
    "number_of_years_of_education",
    # "pop25_high_school",
    # "pop25_no_high_school",
    "pop25_some_college_plus",
]

interactions = [
    'ownership_x_TotOK_cnt',
    'ownership_x_TotOK_Rcnt',
    'ownership_x_TotOK_Rm2',
    "Yrl_savings_$",
    'Inc_x_Consmpt_kwh',
    "Income_x_Suitable_m2",
    'urban_diversity',
    'suburban_diversity',
    'rural_diversity',
]


Util_vars = [
    'West',
    'Mid West',
    'South',
    'NorthEast',
    'High_Solar_Areas',
    'Low_Solar_Areas',
    'DS_HighSolar',
    'Hot_Spots_AvgAr',
    'Hot_Spots_hh',
    'Hot_Spots_hown',
]
IDs = [
    "state",
    "state_abbr",
    'fips',
]
model_dictionaryT = {
    'Personal Characteristics': PerVarB,
    'Financial Resources': FinReB,
    'Suitability For Adoption': SuitRPV,
    'Policy and Financial Incentives': policy_fin,
    'Behavioral Factors': behavior_vT,
    'State_Fixed': state_abrev,
    'Utils': Util_vars,
    'IDS':IDs,
}


model_dictionary = {
    'Personal Characteristics': personals_vars,
    'Financial Resources': Financial_resources,
    'Suitability For Adoption': climate_vars,
    'Policy and Financial Incentives': policy_fin,
    'Behavioral Factors': behavior_v,
    'State_Fixed': state_abrev,
    'Utils': Util_vars,
    'IDS': IDs,
}


high_avg = ['occupation_wholesale_rate', 'occupation_information_rate', 'occupation_finance_rate',
            'occupation_administrative_rate', 'occupation_education_rate', 'occupation_retail_rate']

low_avg = ['occupation_manufacturing_rate', 'occupation_arts_rate', 'occupation_public_rate',
           'occupation_construction_rate',
           'occupation_transportation_rate', 'occupation_agriculture_rate']

high_med = ['occupation_wholesale_rate', 'occupation_information_rate', 'occupation_finance_rate',
            'occupation_administrative_rate', 'occupation_education_rate', 'occupation_manufacturing_rate']
low_med = ['occupation_retail_rate', 'occupation_arts_rate', 'occupation_public_rate', 'occupation_construction_rate',
           'occupation_transportation_rate', 'occupation_agriculture_rate']

targets_B = [
    "Adoption",
    "AvgSres",
    "PV_HuOwn",
    "number_of_solar_system_per_household",
]
target_pHHL = targets_B[3:4]

tomany_missing = [
'pct_eli_hh',
'avg_months_tenancy',
'occ_rate',
'avg_ibi_pct',
'avg_cbi_usd_p_w',
'fmr_2br',
'total_units',
'active_subsidies',
'avg_pbi_usd_p_kwh',
'Adoption_27hh',
'Adoption_27ho',
'aqi_max',
'aqi_90th_percentile',
'aqi_median',
'political_ratio',
'voting_2012_dem_percentage',
'voting_2012_gop_percentage',
]

all_in_model = targets_B + IDs + personals_vars + Financial_resources + climate_vars + policy_fin + behavior_v + edu_vars
all_in_modelHH = ["number_of_solar_system_per_household","PV_HuOwn",] + IDs + personals_vars + Financial_resources + climate_vars + policy_fin + behavior_v + edu_vars

test_vars = target_pHHL + PerVarB + FinReB + SuitRPV + policy_fin + behavior_vT + state_abrev + Util_vars

bb_mod = target_pHHL + PerVarB + FinReP  + SuitRPV + policy_fin + behavior_vT + interactionsp + state_abrev
bb_mod2 = target_pHHL + PerVarB + FinReP  + SuitRPV2 + policy_fin + behavior_vT + interactionsp + state_abrev
pp_mod = target_pHHL + personals_varsp + FinRePp + SuitRPVp +policy_finp + behavior_vp + interactionsp + state_abrev

fin_mod = target_pHHL + FinReP + state_abrev
needs_scaling = [
    #'number_of_solar_system_per_household',
    #'female_pct',
    #'hispanic_pct',
    #'asian_pct',
    #'black_pct',
    #'diversity',
    'age_median',
    'population_density',
    'urban_diversity',
    'rural_diversity',
    'suburban_diversity',
    #'educated_population_rate',
    #'education_bachelor_or_above_rate',
    #'education_bachelor_rate',
    #'education_college_rate',
    #'education_doctoral_rate',
    'pop25_some_college_plus',
    #'household_type_family_rate',
    #'employ_rate',
    'hh_gini_index',
    'median_household_income',
    'hu_med_val',
    'Inc_x_Consmpt_kwh',
    'average_household_size',
    #'hu_own_pct',
    #'occupancy_owner_rate',
    'daily_solar_radiation',
    'cdd',
    'cdd_std',
    #'climate_zone',
    'household_count',
    'hu_2000toafter_pct',
    #'locale_recode(rural)',
    #'locale_recode(suburban)',
    #'URBAN',
    'solar_prod',
    'total_own_Sbldg',
    'total_own_devp',
    'total_own_hh',
    'Tot_own_mw',
    'Yr_own_mwh',
    #'lowincome_tax_credit_bin',
    #'net_metering_bin',
    #'property_tax_bin',
    #'dlrs_kwh',
    #'Policy_Combo',
    'total_own_elep',
    'high_own_elep_hh',
    'low_own_elep_hh',
    'mod_own_elep_hh',
    'verylow_own_elep_hh',
    'Yrl_%_inc',
    'Yrl_savings_$',
    #'travel_time_10_19_rate',
    #'travel_time_20_39_rate',
    #'travel_time_40_89_rate',
    'travel_time_average',
    'ownership_x_TotOK_cnt',
    'ownership_x_TotOK_Rcnt',
    'ownership_x_TotOK_Rm2',
    'Savings_potential',
    'Income_x_EnergyCost',
    'Inc_x_Consmpt_kwh',
    "Income_x_Suitable_m2",
    #'travel_time_less_than_10_rate',
]

to_not_scale = [
    'lowincome_tax_credit_bin',
    "net_metering_bin",
    "property_tax_bin",
    'Policy_Combo',
] + target_pHHL


for v in tomany_missing:
    if v in test_vars:
        del test_vars[test_vars.index(v)]

def conversion_helper(dictionary, searches=[]):
    for s in searches:
        if s not in dictionary:
            newS = input('Give me a new name for {}: '.format(s))
            dictionary[s] = newS
    for v in dictionary:
        print("\t'{}': '{}',".format(v, dictionary[v]))

def col_summation(df, cols, new_name=""):
    if len(new_name) == 0:
        for n in range(len(cols)):
            new_name += cols[n]
            if n < len(cols) - 1:
                new_name += '+'
    df[new_name] = np.zeros(len(df))
    for c in cols:
        df[new_name] += df[c].values
    return df

def col_interaction(df, cols, new_name=""):
    if len(new_name) == 0:
        for n in range(len(cols)):
            new_name += cols[n]
            if n < len(cols) - 1:
                new_name += '+'
    df[new_name] = np.zeros(len(df))
    for c in cols:
        df[new_name] *= df[c].values
    return df