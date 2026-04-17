"""
knowledge_base.py — Comprehensive Medical Knowledge Base
Covers 50+ diseases, symptoms, treatments, medications, and general health topics.
"""

KNOWLEDGE_BASE = [

    # ══════════════════════ RESPIRATORY INFECTIONS ══════════════════════

    {
        "title": "Pneumonia — Complete Guide",
        "category": "infections",
        "text": (
            "Pneumonia is an infection that inflames the air sacs (alveoli) in one or both lungs, causing them to fill with fluid or pus. "
            "It is one of the leading causes of death worldwide, especially in children under 5 and adults over 65. "
            "Types include community-acquired pneumonia (CAP), hospital-acquired pneumonia (HAP), and aspiration pneumonia. "
            "Causes: Bacteria (Streptococcus pneumoniae is most common), viruses (influenza, RSV, COVID-19), fungi (Pneumocystis jirovecii in immunocompromised), and mycoplasma. "
            "Symptoms: persistent cough producing green/yellow/bloody phlegm, fever (38–41°C), chills and shaking, sharp chest pain worse with breathing or coughing, "
            "shortness of breath even at rest, rapid breathing (tachypnea), fatigue and weakness, loss of appetite, nausea, vomiting, confusion (especially elderly). "
            "Diagnosis: chest X-ray shows consolidation or infiltrates, CBC shows elevated WBC (leukocytosis), sputum culture identifies pathogen, "
            "blood cultures, pulse oximetry (SpO2 below 95% is concerning), CT scan for complicated cases. "
            "Treatment: bacterial pneumonia requires antibiotics — amoxicillin 500mg three times daily for mild cases, or amoxicillin-clavulanate 875mg twice daily, "
            "azithromycin 500mg day 1 then 250mg days 2–5, doxycycline 100mg twice daily. "
            "Hospitalized patients receive IV ceftriaxone plus azithromycin. Viral pneumonia is managed with supportive care; "
            "influenza pneumonia may use oseltamivir. Oxygen therapy for SpO2 below 94%. "
            "Complications: sepsis, respiratory failure requiring mechanical ventilation, pleural effusion, lung abscess, bacteremia. "
            "Prevention: pneumococcal vaccine (PCV13 and PPSV23), annual influenza vaccine, COVID-19 vaccine, smoking cessation, good hand hygiene. "
            "Recovery: mild cases 1–3 weeks, severe cases may take 6–8 weeks. "
            "Prognosis depends on age, underlying conditions, and causative organism."
        ),
    },

    {
        "title": "COVID-19 — Comprehensive Overview",
        "category": "infections",
        "text": (
            "COVID-19 is caused by SARS-CoV-2, a novel coronavirus first identified in Wuhan, China in 2019. "
            "It spreads primarily via respiratory droplets and aerosols from infected individuals, with incubation period of 2–14 days (average 5–6 days). "
            "Variants include Alpha, Beta, Delta, and Omicron, each with different transmission and severity profiles. "
            "Symptoms range from mild to severe: fever, dry cough, fatigue, loss of taste (ageusia) and smell (anosmia), "
            "headache, sore throat, muscle aches, runny nose, diarrhea, shortness of breath, chest pain or pressure. "
            "Severe disease: pneumonia, acute respiratory distress syndrome (ARDS), multi-organ failure, cytokine storm. "
            "Risk factors for severe disease: age over 65, obesity, diabetes, hypertension, cardiovascular disease, immunosuppression, chronic lung disease. "
            "Diagnosis: RT-PCR nasal/throat swab (gold standard), rapid antigen tests, chest CT showing bilateral ground-glass opacities. "
            "Blood tests show lymphopenia, elevated CRP, ferritin, D-dimer, IL-6, and LDH in severe cases. "
            "Treatment: mild cases — rest, hydration, paracetamol for fever, isolation for 10 days. "
            "Moderate to severe cases — oxygen therapy, dexamethasone 6mg daily (reduces mortality in ventilated patients), "
            "remdesivir for hospitalized patients requiring oxygen, baricitinib or tocilizumab for cytokine storm. "
            "Anticoagulation with heparin for patients at high VTE risk. "
            "Long COVID (post-acute sequelae): persistent fatigue, brain fog, breathlessness, palpitations lasting weeks to months after acute infection. "
            "Prevention: vaccination (mRNA vaccines — Pfizer/BioNTech, Moderna; viral vector — AstraZeneca, Johnson & Johnson), "
            "wearing masks in crowded indoor spaces, hand washing, ventilation, social distancing. "
            "Vaccines are highly effective against severe disease, hospitalization, and death."
        ),
    },

    {
        "title": "Tuberculosis (TB) — Diagnosis and Treatment",
        "category": "infections",
        "text": (
            "Tuberculosis (TB) is caused by Mycobacterium tuberculosis, a slow-growing airborne bacterium. "
            "It is the world's deadliest infectious disease after COVID-19, killing over 1.5 million people annually. "
            "Primary TB infects the lungs; extrapulmonary TB can affect lymph nodes, pleura, kidneys, spine (Pott's disease), meninges, and other organs. "
            "Latent TB infection (LTBI): bacteria present but not causing active disease; 5–10% lifetime risk of reactivation. "
            "Active TB symptoms: persistent productive cough lasting more than 3 weeks, coughing up blood (hemoptysis), "
            "chest pain, unintentional weight loss, night sweats, fever, chills, fatigue, loss of appetite. "
            "Risk factors: HIV infection (dramatically increases risk), malnutrition, diabetes, chronic kidney disease, "
            "TNF-alpha inhibitors, close contact with active TB cases, living in endemic areas (Sub-Saharan Africa, Southeast Asia, India). "
            "Diagnosis: tuberculin skin test (TST/Mantoux), interferon-gamma release assays (IGRA — QuantiFERON-TB Gold), "
            "chest X-ray showing upper lobe infiltrates, cavitations, calcifications, "
            "sputum smear microscopy (AFB staining), sputum culture on Lowenstein-Jensen medium (6–8 weeks), "
            "GeneXpert MTB/RIF for rapid diagnosis and rifampicin resistance detection. "
            "Treatment — standard regimen (DOTS): 2 months Isoniazid (H) + Rifampicin (R) + Pyrazinamide (Z) + Ethambutol (E), "
            "followed by 4 months Isoniazid + Rifampicin. Total duration 6 months. "
            "Multidrug-resistant TB (MDR-TB) resistant to isoniazid and rifampicin requires 18–24 months of second-line drugs. "
            "Extensively drug-resistant TB (XDR-TB) is even harder to treat. "
            "Latent TB treatment: isoniazid 300mg daily for 6–9 months, or rifampicin for 4 months. "
            "Directly observed therapy (DOT) improves compliance. BCG vaccine protects children against severe forms. "
            "Complications: pleural effusion, respiratory failure, miliary TB (disseminated), TB meningitis."
        ),
    },

    {
        "title": "Influenza (Flu) — Symptoms and Management",
        "category": "infections",
        "text": (
            "Influenza is a highly contagious viral infection caused by influenza A, B, or C viruses. "
            "It spreads through respiratory droplets and can cause seasonal epidemics and occasional pandemics. "
            "Symptoms appear suddenly: high fever (38–40°C), severe headache, muscle aches and pains, extreme fatigue, "
            "dry cough, sore throat, runny or stuffy nose, chills, loss of appetite. "
            "Unlike the common cold, flu symptoms are more severe and sudden. "
            "Complications: bacterial pneumonia (most common serious complication), viral pneumonia, myocarditis, encephalitis, "
            "worsening of chronic conditions (asthma, heart disease, diabetes). "
            "High-risk groups: elderly (65+), young children, pregnant women, immunocompromised, chronic disease patients. "
            "Diagnosis: rapid influenza diagnostic tests (RIDTs), RT-PCR (most accurate), chest X-ray if pneumonia suspected. "
            "Treatment: antivirals most effective within 48 hours of symptoms — oseltamivir (Tamiflu) 75mg twice daily for 5 days, "
            "zanamivir (Relenza) inhaled twice daily, baloxavir marboxil (Xofluza) single dose for uncomplicated influenza. "
            "Symptomatic treatment: paracetamol or ibuprofen for fever and pain, rest, plenty of fluids. "
            "Avoid aspirin in children (Reye's syndrome risk). "
            "Prevention: annual influenza vaccination is the most effective prevention, "
            "good respiratory hygiene, hand washing, staying home when sick."
        ),
    },

    # ══════════════════════ LUNG/TISSUE DISEASES ══════════════════════

    {
        "title": "Lung Cancer — Types, Staging and Treatment",
        "category": "tissue",
        "text": (
            "Lung cancer is the leading cause of cancer-related deaths worldwide, accounting for approximately 1.8 million deaths annually. "
            "Main types: Non-small cell lung cancer (NSCLC) — 85% of cases — includes adenocarcinoma (most common, often in non-smokers), "
            "squamous cell carcinoma (central, linked to smoking), and large cell carcinoma. "
            "Small cell lung cancer (SCLC) — 15% of cases — very aggressive, strongly linked to smoking, often metastatic at diagnosis. "
            "Risk factors: cigarette smoking (accounts for 85% of cases — 15–30x increased risk), secondhand smoke, "
            "radon gas exposure (second leading cause), asbestos, air pollution, genetic predisposition, occupational carcinogens. "
            "Symptoms: persistent cough that worsens over time, coughing up blood (hemoptysis), chest pain, shortness of breath, "
            "hoarseness, unexplained weight loss, fatigue, recurrent respiratory infections, wheezing, difficulty swallowing. "
            "Paraneoplastic syndromes: hypercalcemia (squamous cell), SIADH (SCLC), Cushing's syndrome, Lambert-Eaton syndrome. "
            "Diagnosis: chest X-ray, CT scan of chest with contrast, PET scan for staging, bronchoscopy with biopsy, "
            "CT-guided needle biopsy, sputum cytology, mediastinoscopy, molecular testing (EGFR, ALK, ROS1, PD-L1 expression). "
            "Staging: Stage I (localized), Stage II (regional lymph nodes), Stage III (mediastinal involvement), Stage IV (metastatic). "
            "Treatment by stage and type: Stage I-II NSCLC — surgical resection (lobectomy preferred), stereotactic body radiotherapy (SBRT). "
            "Stage III NSCLC — concurrent chemoradiation (platinum-based chemotherapy + radiotherapy), immunotherapy consolidation (durvalumab). "
            "Stage IV NSCLC — targeted therapy for driver mutations (erlotinib, gefitinib, osimertinib for EGFR; crizotinib for ALK), "
            "immunotherapy (pembrolizumab for high PD-L1 expression), chemotherapy (carboplatin/paclitaxel or pemetrexed). "
            "SCLC — chemotherapy (etoposide + platinum), prophylactic cranial irradiation, immunotherapy. "
            "5-year survival: Stage I 60–80%, Stage IV less than 10%. "
            "Screening: low-dose CT annually for high-risk individuals (smokers aged 50–80, 20+ pack-year history)."
        ),
    },

    {
        "title": "Pulmonary Fibrosis — Causes and Management",
        "category": "tissue",
        "text": (
            "Pulmonary fibrosis is a chronic, progressive lung disease characterized by scarring (fibrosis) of lung tissue, "
            "making breathing increasingly difficult. Idiopathic pulmonary fibrosis (IPF) is the most common form with no known cause. "
            "Other forms: hypersensitivity pneumonitis, drug-induced fibrosis (amiodarone, methotrexate, nitrofurantoin), "
            "connective tissue disease-associated (rheumatoid arthritis, scleroderma, Sjogren's), occupational (asbestosis, silicosis, coal workers' pneumoconiosis). "
            "Symptoms: progressive breathlessness on exertion, dry persistent cough, fatigue, unexplained weight loss, "
            "aching muscles and joints, clubbing of fingers and toes (in advanced disease). "
            "Physical exam: bibasilar inspiratory crackles (Velcro crackles), clubbing. "
            "Pulmonary function tests show restrictive pattern: reduced FVC, TLC, and DLCO. "
            "Diagnosis: high-resolution CT (HRCT) showing usual interstitial pneumonia (UIP) pattern — bilateral basal honeycombing with traction bronchiectasis, "
            "subpleural, basal predominant distribution. Surgical lung biopsy in uncertain cases. "
            "6-minute walk test to assess exercise capacity. "
            "Bronchoalveolar lavage (BAL) to exclude other conditions. "
            "Treatment: antifibrotic drugs slow progression — pirfenidone (reduces FVC decline by ~50%), nintedanib (tyrosine kinase inhibitor). "
            "Lung transplantation is the only cure for eligible patients. "
            "Supplemental oxygen for hypoxemia (SpO2 below 88%). Pulmonary rehabilitation improves quality of life. "
            "Proton pump inhibitors for gastroesophageal reflux (common trigger of acute exacerbations). "
            "Avoid smoking and further lung irritants. Annual influenza and pneumococcal vaccines. "
            "Prognosis: median survival 3–5 years from diagnosis without treatment; antifibrotics extend survival. "
            "Acute exacerbations have high mortality (>50%)."
        ),
    },

    {
        "title": "Pleural Effusion — Causes, Diagnosis, Treatment",
        "category": "tissue",
        "text": (
            "Pleural effusion is abnormal accumulation of fluid in the pleural space (between lung and chest wall). "
            "Classified as transudative or exudative using Light's criteria. "
            "Transudative causes: heart failure (most common overall cause), cirrhosis with portal hypertension, nephrotic syndrome, hypoalbuminemia. "
            "Exudative causes: pneumonia (parapneumonic effusion), malignancy (lung, breast, lymphoma), tuberculosis, pulmonary embolism, "
            "pancreatitis, autoimmune diseases (lupus, rheumatoid arthritis), post-cardiac injury syndrome. "
            "Symptoms depend on size: small effusions may be asymptomatic; larger effusions cause dyspnea, orthopnea, "
            "pleuritic chest pain (sharp, worse with breathing — suggests inflammation), dry cough, fever if infected. "
            "Physical exam: reduced breath sounds at base, dullness to percussion, decreased vocal fremitus, tracheal deviation away (massive effusion). "
            "Diagnosis: chest X-ray shows blunting of costophrenic angle (needs >200ml), layering on lateral decubitus, "
            "ultrasound (most sensitive for small effusions, guides thoracentesis), CT scan defines loculations and underlying cause. "
            "Thoracentesis: send fluid for protein, LDH, glucose, pH, cell count and differential, gram stain and culture, cytology, ADA (TB). "
            "Light's criteria for exudate: fluid:serum protein ratio >0.5, fluid:serum LDH ratio >0.6, fluid LDH >2/3 upper normal serum LDH. "
            "Treatment: treat underlying cause. Therapeutic thoracentesis for symptomatic relief. "
            "Empyema (infected effusion) requires chest tube drainage + antibiotics. "
            "Malignant effusion: repeated thoracentesis, pleurodesis (talc, doxycycline) to prevent reaccumulation, indwelling pleural catheter. "
            "Transudates: treat heart failure (diuretics), cirrhosis, nephrotic syndrome."
        ),
    },

    {
        "title": "Asthma — Management and Treatment Guidelines",
        "category": "respiratory",
        "text": (
            "Asthma is a chronic inflammatory airway disease characterized by reversible airflow obstruction, bronchial hyperresponsiveness, and airway remodeling. "
            "Affects over 300 million people worldwide. "
            "Triggers: allergens (pollen, dust mites, pet dander, mold), respiratory infections, exercise, cold air, smoke, air pollution, "
            "NSAIDs/aspirin (in aspirin-exacerbated respiratory disease), beta-blockers, stress, GERD. "
            "Symptoms: recurrent wheeze, shortness of breath, chest tightness, cough (especially nocturnal and early morning). "
            "Symptoms are typically worse at night and in early morning, and reversible with bronchodilators. "
            "Severity classification: intermittent, mild persistent, moderate persistent, severe persistent. "
            "Diagnosis: spirometry shows obstructive pattern with FEV1/FVC ratio below 0.7, reversibility (>12% and >200ml improvement post-bronchodilator), "
            "peak flow variability >20%, bronchial provocation test (methacholine challenge), FeNO for eosinophilic inflammation. "
            "Treatment (GINA stepwise approach): "
            "Step 1 (intermittent): as-needed SABA (salbutamol/albuterol 100mcg inhaler). "
            "Step 2 (mild persistent): low-dose ICS (budesonide 200–400mcg or beclomethasone 200–500mcg daily). "
            "Step 3 (moderate): low-dose ICS + LABA (formoterol or salmeterol), or medium-dose ICS. "
            "Step 4 (severe): medium-high dose ICS + LABA. "
            "Step 5 (very severe): add LAMA (tiotropium), biologic therapies (omalizumab for allergic, mepolizumab/benralizumab for eosinophilic asthma). "
            "Acute exacerbation: salbutamol nebulization every 20 minutes, ipratropium bromide, systemic corticosteroids (prednisolone 40–50mg for 5 days), "
            "oxygen to maintain SpO2 93–95%, IV magnesium sulfate for severe attacks, ICU for life-threatening attacks. "
            "Education: proper inhaler technique, written action plan, trigger avoidance, smoking cessation."
        ),
    },

    {
        "title": "COPD — Chronic Obstructive Pulmonary Disease",
        "category": "respiratory",
        "text": (
            "COPD is a progressive, largely irreversible airflow limitation caused by chronic bronchitis and/or emphysema. "
            "Fourth leading cause of death worldwide. Strongly linked to tobacco smoking (>80% of cases). "
            "Other causes: occupational dusts and chemicals, biomass fuel exposure (indoor cooking in developing countries), alpha-1 antitrypsin deficiency. "
            "Chronic bronchitis: productive cough for at least 3 months in 2 consecutive years. "
            "Emphysema: destruction of alveolar walls causing air trapping and reduced gas exchange. "
            "Symptoms: progressive dyspnea on exertion (main complaint), chronic cough, sputum production, wheezing, chest tightness. "
            "Signs: barrel chest, prolonged expiration, use of accessory muscles, pursed-lip breathing, peripheral edema (cor pulmonale). "
            "Diagnosis: spirometry is essential — FEV1/FVC <0.70 post-bronchodilator confirms obstruction. "
            "GOLD staging: GOLD 1 (FEV1 ≥80%), GOLD 2 (50–80%), GOLD 3 (30–50%), GOLD 4 (<30%). "
            "Chest X-ray: hyperinflation, flattened diaphragm, increased AP diameter. CT shows emphysematous bullae. "
            "ABG shows hypoxemia; late stages hypercapnia. CBC may show polycythemia. "
            "Treatment: smoking cessation is the single most important intervention. "
            "Bronchodilators: short-acting (salbutamol, ipratropium) for symptom relief, "
            "long-acting (tiotropium, indacaterol, glycopyrronium — LAMA; salmeterol, formoterol, indacaterol — LABA). "
            "ICS added for frequent exacerbators with eosinophilia. Triple therapy (LAMA+LABA+ICS) for severe disease. "
            "Phosphodiesterase-4 inhibitor roflumilast for frequent exacerbations with chronic bronchitis. "
            "Long-term oxygen therapy (>15 hours/day) for PaO2 <55mmHg or SpO2 ≤88% — improves survival. "
            "Pulmonary rehabilitation significantly improves exercise capacity and quality of life. "
            "Exacerbation treatment: increased bronchodilators, systemic corticosteroids, antibiotics (amoxicillin, azithromycin, doxycycline). "
            "Lung volume reduction surgery or bronchoscopic procedures for selected emphysema patients. Lung transplantation for end-stage."
        ),
    },

    # ══════════════════════ CARDIOVASCULAR ══════════════════════

    {
        "title": "Hypertension — High Blood Pressure Management",
        "category": "cardiovascular",
        "text": (
            "Hypertension (high blood pressure) is defined as systolic BP ≥140 mmHg and/or diastolic BP ≥90 mmHg on multiple readings. "
            "It affects over 1.3 billion people worldwide and is a major risk factor for heart attack, stroke, kidney disease, and death. "
            "Classification: Normal <120/80, Elevated 120–129/<80, Stage 1 HTN 130–139/80–89, Stage 2 HTN ≥140/90, Hypertensive crisis ≥180/120. "
            "Primary (essential) hypertension: 90–95% of cases, no identifiable cause. "
            "Secondary hypertension causes: chronic kidney disease, renal artery stenosis, primary aldosteronism, pheochromocytoma, Cushing's syndrome, OSA, thyroid disorders, medications (OCP, NSAIDs, decongestants). "
            "Risk factors: family history, age, obesity, high sodium diet, physical inactivity, excess alcohol, smoking, stress, diabetes, dyslipidemia. "
            "Often asymptomatic — the 'silent killer.' Symptoms when severe: headache (occipital), visual changes, dizziness, nosebleeds, palpitations, shortness of breath. "
            "Hypertensive emergencies: hypertensive encephalopathy, stroke, MI, aortic dissection, acute heart failure. "
            "Diagnosis: accurate BP measurement (at least 2 readings, 2 occasions), ambulatory BP monitoring (ABPM) or home monitoring. "
            "Investigations: urinalysis (proteinuria, hematuria), renal function, electrolytes, fasting glucose, lipid profile, ECG, echocardiogram. "
            "Treatment: lifestyle modifications — DASH diet (low sodium <2g/day, high fruits/vegetables), weight loss, regular aerobic exercise (150 min/week), "
            "limit alcohol, smoking cessation, stress reduction. "
            "First-line medications: thiazide diuretics (hydrochlorothiazide 12.5–25mg), ACE inhibitors (ramipril 5–10mg, lisinopril 10–40mg), "
            "ARBs (losartan 50–100mg, valsartan 80–320mg), calcium channel blockers (amlodipine 5–10mg, nifedipine). "
            "Beta-blockers (atenolol, metoprolol, bisoprolol) for heart failure, post-MI, angina, or rate control. "
            "Target BP: <130/80 for most adults, <140/90 for elderly with frailty. Combination therapy often required. "
            "Monitor: renal function, electrolytes (especially with ACE inhibitors/diuretics), adherence."
        ),
    },

    {
        "title": "Heart Failure — Diagnosis and Management",
        "category": "cardiovascular",
        "text": (
            "Heart failure (HF) is a syndrome where the heart cannot pump enough blood to meet the body's demands. "
            "Affects over 64 million people worldwide. Leading cause of hospitalization in adults over 65. "
            "Classification: HFrEF (EF <40%) — reduced ejection fraction, HFmrEF (EF 40–49%), HFpEF (EF ≥50%) — preserved EF. "
            "Causes: coronary artery disease (most common), hypertension, cardiomyopathy (dilated, hypertrophic, restrictive), "
            "valvular disease, arrhythmias (AF), myocarditis, alcohol, chemotherapy toxicity, thyroid disease. "
            "Symptoms: dyspnea on exertion and at rest, orthopnea (need to prop up with pillows), paroxysmal nocturnal dyspnea, "
            "peripheral edema (ankle swelling), fatigue, reduced exercise tolerance, rapid weight gain, pulmonary edema, ascites. "
            "NYHA classification: Class I (no symptoms with ordinary activity), II (slight limitation), III (marked limitation), IV (symptoms at rest). "
            "Diagnosis: echocardiogram (gold standard — assesses EF and structure), BNP or NT-proBNP elevated (>100 pg/mL and >125 pg/mL), "
            "chest X-ray (cardiomegaly, pulmonary congestion, pleural effusions, Kerley B lines), ECG, cardiac MRI. "
            "Treatment of HFrEF (evidence-based four pillars): "
            "1. ACE inhibitors or ARBs (ramipril, enalapril, valsartan) — reduce mortality 20–25%. "
            "2. Beta-blockers (bisoprolol, carvedilol, metoprolol succinate) — reduce mortality 34%. "
            "3. Mineralocorticoid receptor antagonists (spironolactone, eplerenone) — reduce mortality 30%. "
            "4. SGLT2 inhibitors (dapagliflozin, empagliflozin) — reduce hospitalization and cardiovascular death. "
            "Also: loop diuretics (furosemide) for fluid overload, ivabradine for high heart rate, ARNI (sacubitril/valsartan). "
            "Device therapy: ICD for sudden death prevention (EF <35%), CRT for LBBB (EF <35%). "
            "HFpEF: treat underlying causes, symptom management with diuretics, control BP and AF, SGLT2 inhibitors show benefit."
        ),
    },

    {
        "title": "Coronary Artery Disease and Heart Attack",
        "category": "cardiovascular",
        "text": (
            "Coronary artery disease (CAD) results from atherosclerotic plaque buildup in coronary arteries, reducing blood flow to the myocardium. "
            "Acute myocardial infarction (AMI) occurs when a plaque ruptures, causing thrombotic occlusion. "
            "STEMI (ST-elevation MI) — complete occlusion requiring emergency reperfusion. "
            "NSTEMI/UA (non-ST-elevation MI/unstable angina) — partial occlusion. "
            "Risk factors: hypertension, hyperlipidemia, diabetes, smoking, family history, obesity, physical inactivity, age (men >45, women >55), "
            "metabolic syndrome, chronic kidney disease, inflammatory conditions. "
            "Symptoms of angina: chest pain or pressure (crushing, squeezing, heavy) radiating to left arm, jaw, neck, or back; "
            "triggered by exertion or emotion, relieved by rest or nitrates; lasting 2–10 minutes. "
            "NSTEMI symptoms: similar but more severe or at rest, lasting longer. "
            "STEMI: severe persistent chest pain >20 minutes, sweating, nausea, dizziness, sense of doom. "
            "Silent MI: diabetics and elderly may have atypical or no symptoms. "
            "Diagnosis: ECG (ST elevation in STEMI, ST depression/T-wave changes in NSTEMI), "
            "cardiac biomarkers (troponin I/T — rises within 3–6 hours, peaks 12–24 hours, returns to normal 5–14 days; CK-MB), "
            "echocardiogram (wall motion abnormalities), coronary angiography (gold standard). "
            "STEMI treatment: primary PCI (percutaneous coronary intervention) within 90 minutes of first medical contact. "
            "Thrombolysis if PCI not available within 120 minutes (tenecteplase, streptokinase). "
            "Aspirin 300mg loading + ticagrelor 180mg or clopidogrel 600mg, anticoagulation (heparin, enoxaparin). "
            "Post-MI secondary prevention: dual antiplatelet therapy for 12 months, lifelong aspirin, statin (atorvastatin 80mg), "
            "ACE inhibitor, beta-blocker, aldosterone antagonist if EF reduced, cardiac rehabilitation."
        ),
    },

    # ══════════════════════ DIABETES & ENDOCRINE ══════════════════════

    {
        "title": "Type 2 Diabetes Mellitus — Complete Management",
        "category": "endocrine",
        "text": (
            "Type 2 diabetes (T2DM) is a metabolic disorder characterized by insulin resistance and progressive beta-cell dysfunction, "
            "resulting in chronic hyperglycemia. Affects over 500 million people worldwide. "
            "Risk factors: obesity (especially central adiposity), physical inactivity, family history, age >45, gestational diabetes history, "
            "prediabetes, polycystic ovary syndrome, ethnicity (South Asian, African, Hispanic). "
            "Symptoms: polyuria, polydipsia, polyphagia, unexplained weight loss, fatigue, blurred vision, slow-healing wounds, "
            "recurrent infections, numbness/tingling in extremities. Often asymptomatic for years. "
            "Diagnosis: fasting plasma glucose ≥126 mg/dL (7.0 mmol/L), 2-hour post-load glucose ≥200 mg/dL (11.1 mmol/L), "
            "HbA1c ≥6.5% (48 mmol/mol), random glucose ≥200 mg/dL with symptoms. "
            "Prediabetes: fasting glucose 100–125 mg/dL (5.6–6.9 mmol/L) or HbA1c 5.7–6.4%. "
            "Monitoring: HbA1c every 3 months (target <7% for most, <8% for elderly/comorbidities), fasting glucose, self-monitoring of blood glucose, "
            "annual lipid profile, kidney function (eGFR, urine albumin:creatinine ratio), ophthalmology, foot examination, BP. "
            "Treatment — lifestyle first: medical nutrition therapy (low carbohydrate or Mediterranean diet), "
            "150 minutes moderate aerobic exercise weekly, weight loss (10% body weight improves glycemic control significantly). "
            "Pharmacotherapy: metformin 500–2000mg daily (first-line, weight neutral, cheap, reduces CV events), "
            "SGLT2 inhibitors (empagliflozin, dapagliflozin — cardiovascular and renal protection, weight loss, reduce hospitalization in heart failure), "
            "GLP-1 receptor agonists (semaglutide, liraglutide — weight loss, cardiovascular benefit, injectable or oral semaglutide), "
            "DPP-4 inhibitors (sitagliptin, saxagliptin — weight neutral, well tolerated), "
            "sulfonylureas (glipizide, gliclazide — cheap, risk of hypoglycemia), "
            "insulin (basal insulin glargine/detemir starting at 10 units at bedtime, titrate by 2 units every 3 days). "
            "Complications: microvascular — diabetic retinopathy (leading cause of blindness), nephropathy (leading cause of dialysis), "
            "peripheral neuropathy, autonomic neuropathy. "
            "Macrovascular — cardiovascular disease (2–4x increased risk), stroke, peripheral artery disease. "
            "Diabetic foot: regular examination, proper footwear, prompt wound care. Hyperosmolar hyperglycemic state: emergency treatment with IV fluids and insulin."
        ),
    },

    {
        "title": "Type 1 Diabetes Mellitus",
        "category": "endocrine",
        "text": (
            "Type 1 diabetes (T1DM) is an autoimmune disease where T-cells destroy pancreatic beta cells, causing absolute insulin deficiency. "
            "Accounts for 5–10% of all diabetes. Onset typically in childhood or young adulthood but can occur at any age. "
            "Pathophysiology: genetic susceptibility (HLA-DR3, HLA-DR4) plus environmental trigger (viral infection — enterovirus, rotavirus) "
            "leads to autoimmune destruction. Autoantibodies: anti-islet cell antibodies (ICA), anti-GAD65, anti-insulin (IAA), anti-IA2. "
            "Symptoms: acute onset polyuria, polydipsia, polyphagia, weight loss, fatigue. Often presents in diabetic ketoacidosis (DKA). "
            "DKA: hyperglycemia (>250 mg/dL), metabolic acidosis (pH <7.3), ketonemia/ketonuria, nausea, vomiting, abdominal pain, "
            "fruity breath (acetone), Kussmaul breathing, dehydration, altered consciousness. "
            "DKA treatment: IV fluids (0.9% saline), IV insulin infusion, potassium replacement (critical — insulin drives K+ into cells), "
            "monitor glucose hourly, bicarbonate only for pH <6.9. "
            "Insulin regimens: basal-bolus therapy (long-acting basal insulin — glargine or degludec, plus rapid-acting bolus — lispro, aspart, or glulisine with meals). "
            "Insulin pump therapy (CSII) and continuous glucose monitoring (CGM) for better control. "
            "Closed-loop systems (artificial pancreas) combining CGM and insulin pump. "
            "HbA1c target: <7% for most, individual targets based on hypoglycemia risk. "
            "Hypoglycemia: blood glucose <70 mg/dL, symptoms tremor, sweating, palpitations, confusion; treat with 15g fast-acting carbohydrates. "
            "Severe hypoglycemia: unconscious, give glucagon injection or IV dextrose. "
            "Complications same as T2DM. Celiac disease and thyroid disease more common in T1DM (autoimmune association). "
            "Annual screening: HbA1c, renal function, eye exam, feet, thyroid, celiac."
        ),
    },

    {
        "title": "Thyroid Diseases — Hypothyroidism and Hyperthyroidism",
        "category": "endocrine",
        "text": (
            "Thyroid disorders are among the most common endocrine conditions. "
            "Hypothyroidism: underactive thyroid, insufficient thyroid hormone production. "
            "Causes: Hashimoto's thyroiditis (autoimmune, most common in iodine-sufficient areas), iodine deficiency (most common worldwide), "
            "post-thyroidectomy, radioiodine treatment, medications (amiodarone, lithium), central hypothyroidism. "
            "Symptoms: fatigue, weight gain, cold intolerance, constipation, dry skin and hair, hair loss, depression, bradycardia, "
            "menstrual irregularities, hoarseness, myxedema (severe), pericardial effusion, elevated cholesterol. "
            "Diagnosis: elevated TSH (>4.5 mIU/L), low free T4; anti-TPO antibodies in Hashimoto's. "
            "Treatment: levothyroxine (T4), start low 25–50 mcg, increase every 4–6 weeks to achieve TSH 0.5–2.5 mIU/L. "
            "Taken on empty stomach 30–60 minutes before food. "
            "Hyperthyroidism: overactive thyroid, excess thyroid hormone. "
            "Causes: Graves' disease (autoimmune, TSH receptor stimulating antibodies), toxic multinodular goiter, toxic adenoma, "
            "thyroiditis (subacute, postpartum), iodine-induced, factitious. "
            "Symptoms: weight loss despite increased appetite, heat intolerance, sweating, palpitations, tachycardia (AF in elderly), "
            "tremor, anxiety, insomnia, frequent bowel movements, menstrual irregularities, eye changes (Graves' ophthalmopathy — exophthalmos), goiter. "
            "Diagnosis: low TSH, elevated free T4 and/or T3; TSH receptor antibodies (TRAb) for Graves'. Thyroid scan, ultrasound. "
            "Treatment: anti-thyroid drugs (carbimazole, methimazole, propylthiouracil), radioiodine ablation, thyroidectomy. "
            "Propranolol for symptom control (tremor, palpitations). Thyroid storm: life-threatening, requires ICU."
        ),
    },

    # ══════════════════════ NEUROLOGICAL ══════════════════════

    {
        "title": "Stroke — Recognition, Types and Treatment",
        "category": "neurology",
        "text": (
            "Stroke is a medical emergency caused by disruption of blood supply to the brain. "
            "Second leading cause of death and leading cause of disability worldwide. "
            "Types: ischemic stroke (87%) — thrombotic or embolic; hemorrhagic stroke (13%) — intracerebral or subarachnoid. "
            "FAST recognition: Face drooping, Arm weakness, Speech difficulty, Time to call emergency. "
            "Additional symptoms: sudden severe headache ('thunderclap' in SAH), vision loss, vertigo, ataxia, confusion, altered consciousness. "
            "Transient ischemic attack (TIA): stroke symptoms lasting <24 hours (usually <1 hour), high risk of subsequent stroke. "
            "Risk factors: hypertension (most important modifiable), atrial fibrillation, diabetes, hyperlipidemia, smoking, obesity, "
            "carotid artery disease, previous stroke/TIA, heart disease, oral contraceptives (in young women), hypercoagulable states. "
            "Diagnosis: non-contrast CT (rules out hemorrhage immediately), MRI-DWI (detects ischemia within minutes), "
            "CT angiography or MRA (identifies vessel occlusion), carotid Doppler, echocardiogram, 24-hour Holter (for AF detection). "
            "Ischemic stroke treatment: IV thrombolysis with alteplase (tPA) within 4.5 hours of onset (if no contraindications, BP <185/110, no bleeding), "
            "mechanical thrombectomy (stent retriever) within 24 hours for large vessel occlusion — dramatic improvement in outcomes. "
            "Aspirin 300mg within 48 hours (not if thrombolysis given — wait 24 hours). "
            "Blood pressure management: allow permissive hypertension in acute phase unless >220/120. "
            "Secondary prevention: antiplatelet therapy (aspirin 75–100mg + clopidogrel for 90 days, then aspirin alone), "
            "anticoagulation for AF (warfarin or NOACs — apixaban, rivaroxaban, dabigatran), statin therapy, "
            "BP control, smoking cessation, AF management, carotid endarterectomy if >70% stenosis. "
            "Rehabilitation: physiotherapy, speech therapy, occupational therapy — crucial for functional recovery."
        ),
    },

    {
        "title": "Epilepsy — Seizure Management",
        "category": "neurology",
        "text": (
            "Epilepsy is a neurological disorder characterized by recurrent unprovoked seizures due to abnormal electrical activity in the brain. "
            "Affects over 50 million people worldwide. "
            "Classification: focal seizures (start in one brain area — awareness preserved or impaired), generalized seizures (both hemispheres — absence, myoclonic, tonic-clonic). "
            "Status epilepticus: seizure lasting >5 minutes or recurrent seizures without recovery — medical emergency. "
            "Causes: idiopathic (genetic), structural (tumor, stroke, trauma, cortical malformation), metabolic (hyponatremia, hypoglycemia, uremia), "
            "infections (meningitis, encephalitis), autoimmune, unknown. "
            "Triggers: sleep deprivation, stress, alcohol, flashing lights (photosensitive), missed medication, fever. "
            "Diagnosis: EEG (essential — shows epileptiform discharges), MRI brain (structural cause), blood tests, "
            "video-EEG for classification, genetic testing. "
            "First-line anti-epileptic drugs (AEDs): levetiracetam (broad spectrum, minimal drug interactions, safest in pregnancy), "
            "sodium valproate (most effective broad-spectrum but teratogenic), lamotrigine (well tolerated, good for focal and generalized), "
            "carbamazepine (focal seizures), oxcarbazepine. "
            "Focal epilepsy: carbamazepine, lamotrigine, levetiracetam, lacosamide. "
            "Absence epilepsy: ethosuximide, valproate. "
            "Status epilepticus treatment: lorazepam IV (first-line), then phenytoin/fosphenytoin IV, then general anesthesia (propofol, thiopental). "
            "60–70% achieve seizure freedom with medication. "
            "Drug-resistant epilepsy (2 failed AEDs): ketogenic diet, vagus nerve stimulation, responsive neurostimulation, surgery (if defined focus). "
            "SUDEP (sudden unexpected death in epilepsy): rare but real risk, reduced by good seizure control."
        ),
    },

    # ══════════════════════ GASTROINTESTINAL ══════════════════════

    {
        "title": "Gastroesophageal Reflux Disease (GERD)",
        "category": "gastroenterology",
        "text": (
            "GERD occurs when stomach acid repeatedly flows back into the esophagus, irritating its lining. "
            "Affects 20% of Western populations. "
            "Pathophysiology: lower esophageal sphincter (LES) dysfunction, transient LES relaxations, hiatal hernia (displacement of stomach above diaphragm), "
            "impaired esophageal clearance, delayed gastric emptying. "
            "Symptoms: heartburn (burning sensation rising from stomach to chest, worse after eating, lying down, or bending), "
            "acid regurgitation (sour or bitter taste), dysphagia, odynophagia, chest pain (can mimic cardiac pain), "
            "laryngopharyngeal reflux (hoarseness, chronic cough, throat clearing, globus). "
            "Alarm symptoms (require urgent endoscopy): dysphagia, weight loss, anemia, hematemesis, melena, age >55 with new symptoms. "
            "Complications: esophagitis, peptic stricture, Barrett's esophagus (columnar metaplasia — precancerous), esophageal adenocarcinoma. "
            "Diagnosis: clinical diagnosis in typical cases; 24-hour pH-impedance monitoring (gold standard), upper endoscopy (for complications/Barrett's screening). "
            "Treatment: lifestyle modifications — lose weight, elevate head of bed 15–20cm, avoid large meals, "
            "avoid trigger foods (fatty/spicy food, chocolate, coffee, alcohol, citrus, tomatoes), avoid eating within 3 hours of bedtime, quit smoking. "
            "Step-up pharmacotherapy: antacids for mild symptoms, H2 blockers (ranitidine, famotidine) for mild-moderate, "
            "proton pump inhibitors (omeprazole 20–40mg, lansoprazole, pantoprazole, esomeprazole) for moderate-severe — most effective, "
            "take 30–60 minutes before breakfast. "
            "Surgical: Nissen fundoplication for refractory GERD or large hiatal hernia. "
            "Barrett's esophagus: regular endoscopic surveillance, high-grade dysplasia treated with radiofrequency ablation or endoscopic resection."
        ),
    },

    {
        "title": "Peptic Ulcer Disease",
        "category": "gastroenterology",
        "text": (
            "Peptic ulcer disease (PUD) involves ulcers (mucosal defects >5mm) in the stomach (gastric ulcers) or duodenum (duodenal ulcers). "
            "Causes: Helicobacter pylori infection (60–70% of gastric, 90–95% of duodenal ulcers), "
            "NSAIDs/aspirin (inhibit COX-1, reduce prostaglandins — impair mucosal protection), "
            "rarely Zollinger-Ellison syndrome (gastrinoma). "
            "Symptoms: epigastric pain (burning or gnawing), duodenal ulcer pain relieved by food (hungry pain), gastric ulcer pain worsened by food, "
            "nausea, vomiting, bloating, early satiety. "
            "Complications: bleeding (hematemesis, melena — most common complication), perforation (sudden severe abdominal pain, rigid abdomen), "
            "pyloric stenosis (gastric outlet obstruction — vomiting, weight loss). "
            "Diagnosis: upper endoscopy (EGD — gold standard, allows biopsy for H. pylori and malignancy), "
            "barium swallow, H. pylori testing (urea breath test, stool antigen, CLO test during endoscopy, serology). "
            "Treatment: H. pylori eradication — triple therapy: PPI + clarithromycin + amoxicillin for 14 days (80–85% eradication), "
            "or bismuth quadruple therapy (PPI + bismuth + metronidazole + tetracycline) for clarithromycin-resistant areas. "
            "Acid suppression: PPI for 4–8 weeks (omeprazole 20–40mg, lansoprazole 30mg). "
            "NSAID-induced ulcers: stop NSAID if possible, use selective COX-2 inhibitor with PPI if NSAID needed. "
            "Upper GI bleed management: endoscopy for diagnosis and treatment (injection, thermal, clips), "
            "IV PPI infusion (omeprazole 80mg bolus then 8mg/hour), blood transfusion, surgery for refractory bleeding."
        ),
    },

    # ══════════════════════ KIDNEYS ══════════════════════

    {
        "title": "Chronic Kidney Disease (CKD)",
        "category": "nephrology",
        "text": (
            "Chronic kidney disease (CKD) is defined as kidney damage or GFR <60 mL/min/1.73m² for ≥3 months. "
            "Affects over 800 million people globally. Leading causes of end-stage renal disease (ESRD) requiring dialysis or transplant. "
            "Causes: diabetic nephropathy (most common — 40%), hypertensive nephrosclerosis, glomerulonephritis, "
            "polycystic kidney disease, obstructive uropathy, recurrent infections, medications (NSAIDs, aminoglycosides, contrast). "
            "KDIGO staging by GFR: G1 (≥90), G2 (60–89), G3a (45–59), G3b (30–44), G4 (15–29), G5 (<15 — kidney failure). "
            "Also staged by albuminuria: A1 (<30 mg/g), A2 (30–300), A3 (>300). "
            "Symptoms: often asymptomatic early; later — fatigue, reduced appetite, nausea, vomiting, itching (pruritus), "
            "swelling (edema), hypertension, anemia, bone pain (renal osteodystrophy), reduced urine output, uremic symptoms (encephalopathy, pericarditis). "
            "Complications: hypertension, anemia (low erythropoietin), metabolic acidosis, hyperkalemia, hyperphosphatemia, "
            "hypocalcemia, secondary hyperparathyroidism, cardiovascular disease (main cause of death in CKD), infections. "
            "Diagnosis: serum creatinine, eGFR calculation (CKD-EPI equation), urine albumin:creatinine ratio, urine protein:creatinine ratio, "
            "renal ultrasound (small kidneys in CKD), kidney biopsy for uncertain cause. "
            "Treatment: treat underlying cause (tight BP and glucose control in diabetic nephropathy), "
            "BP target <130/80 with ACE inhibitor or ARB (reduces proteinuria and slows progression — avoid in bilateral renal artery stenosis), "
            "SGLT2 inhibitors (dapagliflozin, canagliflozin — proven to slow CKD progression), "
            "low protein diet (0.6–0.8g/kg/day), fluid and electrolyte management, "
            "erythropoiesis-stimulating agents (ESA) for anemia (target Hb 10–12 g/dL), IV iron supplementation, "
            "phosphate binders (calcium carbonate, sevelamer), vitamin D supplementation, bicarbonate for acidosis. "
            "Renal replacement therapy: hemodialysis (3x/week), peritoneal dialysis, kidney transplantation (best outcomes)."
        ),
    },

    # ══════════════════════ MENTAL HEALTH ══════════════════════

    {
        "title": "Depression — Diagnosis and Treatment",
        "category": "psychiatry",
        "text": (
            "Major depressive disorder (MDD) is a common and serious mental health condition affecting over 280 million people worldwide. "
            "Leading cause of disability globally. "
            "Diagnostic criteria (DSM-5): at least 5 symptoms for 2+ weeks including depressed mood or loss of interest/pleasure plus: "
            "significant weight change, insomnia or hypersomnia, psychomotor agitation or retardation, fatigue, feelings of worthlessness or guilt, "
            "difficulty concentrating, recurrent thoughts of death or suicide. "
            "Subtypes: melancholic, atypical, psychotic, seasonal (SAD), postpartum. "
            "Risk factors: family history, previous episodes, chronic illness, trauma, substance abuse, social isolation, female sex (2x risk). "
            "Screening tools: PHQ-9 (0–27 scale), Beck Depression Inventory, Hamilton Rating Scale. "
            "Differential: hypothyroidism (check TSH), anemia, vitamin B12/D deficiency, substance misuse, bipolar disorder. "
            "Treatment: mild — psychotherapy alone (CBT most evidence-based, IPT, behavioral activation); "
            "moderate-severe — antidepressants + psychotherapy superior to either alone. "
            "First-line antidepressants: SSRIs — fluoxetine 20–60mg, sertraline 50–200mg, escitalopram 10–20mg, citalopram 20–40mg. "
            "SNRIs — venlafaxine 75–225mg, duloxetine 60–120mg (also effective for pain). "
            "Mirtazapine (weight gain, sedation — useful for insomnia and poor appetite). "
            "TCAs (amitriptyline, nortriptyline) — effective but side effects limit use. "
            "MAOIs — reserved for treatment-resistant cases. "
            "Treatment-resistant depression: augmentation (lithium, atypical antipsychotics, T3 thyroid), switch antidepressant, "
            "ketamine/esketamine (rapid onset, for suicidal ideation), ECT (electroconvulsive therapy — most effective for severe/psychotic). "
            "Duration: minimum 6–9 months after remission; 2+ years for recurrent depression. "
            "Always assess suicide risk. Refer to psychiatry for complex cases."
        ),
    },

    {
        "title": "Anxiety Disorders — Overview and Management",
        "category": "psychiatry",
        "text": (
            "Anxiety disorders are the most common mental health conditions, affecting 30% of adults at some point. "
            "Types: generalized anxiety disorder (GAD), panic disorder, social anxiety disorder, specific phobias, "
            "separation anxiety, agoraphobia. "
            "GAD: excessive, uncontrollable worry about multiple domains lasting ≥6 months with physical symptoms (muscle tension, fatigue, concentration difficulties, sleep disturbance, irritability). "
            "Panic disorder: recurrent unexpected panic attacks (intense fear with palpitations, sweating, trembling, shortness of breath, chest pain, derealization, fear of dying or losing control). "
            "Social anxiety: intense fear of social situations, fear of negative evaluation. "
            "PTSD: develops after traumatic event — intrusive memories, avoidance, negative mood, hyperarousal. "
            "Assessment tools: GAD-7 for anxiety, PCL-5 for PTSD, PHQ-PD for panic. "
            "Treatment: CBT (cognitive behavioral therapy) is most evidence-based, most effective in combination with medication. "
            "Pharmacotherapy: SSRIs (sertraline, escitalopram, paroxetine — first-line for all anxiety disorders), "
            "SNRIs (venlafaxine for GAD and social anxiety), "
            "buspirone (for GAD — non-sedating, no abuse potential), "
            "pregabalin (for GAD — faster onset), "
            "short-term benzodiazepines (lorazepam, diazepam) for acute severe anxiety only — risk of dependence, not recommended long-term. "
            "Beta-blockers (propranolol) for performance anxiety (situational only). "
            "Lifestyle: regular aerobic exercise (equivalent to medication for mild anxiety), mindfulness meditation, breathing exercises, "
            "adequate sleep, limit caffeine and alcohol."
        ),
    },

    # ══════════════════════ INFECTIOUS DISEASES ══════════════════════

    {
        "title": "Urinary Tract Infections (UTI)",
        "category": "infectious",
        "text": (
            "UTIs are among the most common bacterial infections, particularly in women (50% lifetime risk). "
            "Types: uncomplicated (cystitis — lower UTI, pyelonephritis — upper UTI), complicated (structural abnormality, catheter, pregnancy, immunocompromised, male). "
            "Pathogens: E. coli (80% of community UTIs), Klebsiella, Proteus, Staphylococcus saprophyticus (young women), Enterococcus. "
            "Cystitis symptoms: dysuria (painful urination), frequency, urgency, suprapubic pain, cloudy or malodorous urine, hematuria. "
            "Pyelonephritis: fever (>38°C), rigors, flank pain, costovertebral angle tenderness, nausea, vomiting, plus lower UTI symptoms. "
            "Diagnosis: urine dipstick (nitrites and leukocyte esterase), urinalysis, urine culture and sensitivity (gold standard — send before antibiotics). "
            "Imaging: ultrasound or CT for complicated/recurrent UTI, obstruction, or suspected abscess. "
            "Treatment of uncomplicated cystitis: nitrofurantoin 100mg BD for 5 days (first choice if GFR >45), "
            "trimethoprim 200mg BD for 7 days, pivmecillinam, fosfomycin 3g single dose. "
            "Avoid fluoroquinolones for uncomplicated UTI (resistance, side effects). "
            "Pyelonephritis (outpatient): ciprofloxacin 500mg BD for 7 days or co-amoxiclav 625mg TID for 14 days. "
            "Hospitalized pyelonephritis: IV ceftriaxone 1–2g daily, step down to oral when improving. "
            "Recurrent UTI prevention: adequate hydration, urinate after intercourse, wipe front to back, cranberry products (modest benefit), "
            "low-dose prophylactic antibiotics, topical vaginal estrogen for postmenopausal women, D-mannose supplementation."
        ),
    },

    {
        "title": "Sepsis and Septic Shock — Emergency Management",
        "category": "infectious",
        "text": (
            "Sepsis is a life-threatening organ dysfunction caused by a dysregulated host response to infection. "
            "Septic shock: subset with profound circulatory, cellular, and metabolic abnormalities with higher mortality. "
            "Mortality: sepsis 10%, septic shock 40–50%. Over 30 million cases annually worldwide. "
            "Common sources: pneumonia (most common), urinary tract, abdominal (peritonitis, cholangitis), skin/soft tissue, meningitis, endocarditis, line infection. "
            "SOFA score used to define organ dysfunction. "
            "qSOFA (quick SOFA) for screening: respiratory rate ≥22, altered mentation, systolic BP ≤100 — ≥2 points warrants concern. "
            "Septic shock criteria: sepsis + vasopressors needed to maintain MAP ≥65 mmHg + serum lactate >2 mmol/L despite adequate fluid resuscitation. "
            "Surviving Sepsis Campaign — Hour-1 Bundle: "
            "1. Measure lactate (repeat if >2 mmol/L). "
            "2. Blood cultures (at least 2 sets) before antibiotics. "
            "3. Broad-spectrum antibiotics within 1 hour (piperacillin-tazobactam + vancomycin, or meropenem for resistant organisms). "
            "4. 30 mL/kg IV crystalloid (0.9% saline or Ringer's lactate) for hypotension or lactate ≥4 mmol/L. "
            "5. Vasopressors (norepinephrine first choice) if MAP <65 mmHg despite fluids. "
            "Additional: vasopressin for refractory shock, hydrocortisone 200mg/day for steroid-responsive shock, "
            "source control (drainage, debridement), blood glucose control (target 6–10 mmol/L), "
            "lung-protective ventilation for ARDS (low tidal volume 6 mL/kg), VTE prophylaxis, stress ulcer prophylaxis."
        ),
    },

    # ══════════════════════ MUSCULOSKELETAL ══════════════════════

    {
        "title": "Rheumatoid Arthritis — Diagnosis and Treatment",
        "category": "rheumatology",
        "text": (
            "Rheumatoid arthritis (RA) is a chronic systemic autoimmune inflammatory disease primarily affecting synovial joints. "
            "Affects 1% of the population; more common in women (3:1 ratio). Peak onset 40–60 years. "
            "Pathophysiology: T-cell mediated immune response, B-cell autoantibodies (RF, anti-CCP), synovial proliferation (pannus formation), cartilage and bone erosion. "
            "Symptoms: symmetric polyarthritis affecting small joints of hands (MCPs, PIPs) and feet, wrists, elbows, knees, ankles. "
            "Morning stiffness lasting >1 hour (key feature), joint swelling, tenderness, warmth, fatigue, low-grade fever, weight loss. "
            "Extra-articular manifestations: rheumatoid nodules (elbows, extensor surfaces), pleural/pericardial effusion, "
            "interstitial lung disease, Sjogren's overlap, vasculitis, scleritis, Felty's syndrome. "
            "Diagnosis: 2010 ACR/EULAR criteria (≥6 points); anti-CCP antibodies (most specific — positive in 70%), "
            "rheumatoid factor (RF) less specific, elevated CRP and ESR, anemia of chronic disease, "
            "X-rays (periarticular osteopenia, joint space narrowing, erosions — late changes), MRI for early erosions. "
            "Treatment — treat-to-target (remission or low disease activity as target): "
            "NSAIDs for symptom relief. Corticosteroids (prednisolone) for bridging or flares. "
            "DMARDs — conventional: methotrexate (first-line, 15–25mg weekly + folic acid), hydroxychloroquine, sulfasalazine, leflunomide. "
            "Biologic DMARDs for inadequate response to csDMARDs: TNF inhibitors (etanercept, adalimumab, infliximab, certolizumab), "
            "IL-6 inhibitors (tocilizumab, sarilumab), abatacept (CTLA4-Ig), rituximab (anti-CD20). "
            "JAK inhibitors (tofacitinib, baricitinib, upadacitinib) — oral targeted therapy. "
            "Physiotherapy, occupational therapy, joint protection strategies, surgery (joint replacement) for severe destruction."
        ),
    },

    {
        "title": "Osteoporosis — Prevention and Treatment",
        "category": "rheumatology",
        "text": (
            "Osteoporosis is a skeletal disorder characterized by low bone mass and microarchitectural deterioration, increasing fracture risk. "
            "Affects 200 million people globally; causes 9 million fractures annually. "
            "T-score (DXA bone density): normal ≥-1.0, osteopenia -1.0 to -2.5, osteoporosis ≤-2.5. "
            "Risk factors: female sex, age, menopause (estrogen deficiency), low BMI, family history of hip fracture, "
            "previous fragility fracture, glucocorticoid use (>7.5mg prednisolone >3 months), smoking, excess alcohol, "
            "low calcium/vitamin D intake, sedentary lifestyle, medical conditions (hyperparathyroidism, hypogonadism, malabsorption, RA, CKD). "
            "Fragility fractures most common: vertebral (back pain, height loss, kyphosis), hip (highest mortality — 20–30% die within a year), wrist (Colles'), humerus. "
            "Diagnosis: DXA scan of lumbar spine and femoral neck, FRAX tool (10-year fracture probability), vertebral fracture assessment. "
            "Treatment: lifestyle — adequate calcium (1000–1200mg/day from diet or supplement), vitamin D (800–1000 IU/day), "
            "weight-bearing exercise, fall prevention, stop smoking, limit alcohol. "
            "Pharmacotherapy: bisphosphonates first-line (alendronate 70mg weekly, risedronate 35mg weekly, zoledronic acid 5mg IV annually), "
            "denosumab (RANKL inhibitor, 60mg SC every 6 months — do not stop abruptly, rebound fractures), "
            "teriparatide/abaloparatide (PTH analogue — anabolic, for severe osteoporosis, 18–24 months), "
            "romosozumab (sclerostin inhibitor — dual anabolic/antiresorptive). "
            "HRT for postmenopausal women with menopausal symptoms. "
            "Hip protectors, home hazard assessment for fall prevention. Review at 3–5 years."
        ),
    },

    # ══════════════════════ HEMATOLOGY ══════════════════════

    {
        "title": "Anemia — Types, Causes and Treatment",
        "category": "hematology",
        "text": (
            "Anemia is defined as hemoglobin below normal: men <13 g/dL, women <12 g/dL, pregnant <11 g/dL. "
            "WHO estimates 1.6 billion people affected globally. "
            "Classification by MCV: microcytic (MCV <80 fL), normocytic (80–100), macrocytic (>100). "
            "Iron deficiency anemia (IDA) — most common worldwide: microcytic hypochromic, low ferritin (<15 ng/mL), low serum iron, high TIBC. "
            "Causes: inadequate intake, malabsorption (celiac disease, gastrectomy), blood loss (menorrhagia, GI bleeding from ulcer, colon cancer, hookworm). "
            "Symptoms of anemia: fatigue, weakness, pallor, dyspnea on exertion, palpitations, dizziness, headache, reduced concentration, tachycardia. "
            "Severe anemia: heart failure, angina, syncope. "
            "IDA specific: koilonychia (spoon nails), angular stomatitis, glossitis, pica, Plummer-Vinson syndrome (dysphagia + IDA). "
            "IDA treatment: treat underlying cause, oral iron (ferrous sulfate 200mg TID or ferrous fumarate 210mg BD — take with vitamin C, avoid with tea/milk), "
            "IV iron (iron sucrose, ferric carboxymaltose) for malabsorption, intolerance, or rapid correction. Recheck after 4–6 weeks. "
            "B12 deficiency anemia: macrocytic (megaloblastic), causes pernicious anemia (anti-intrinsic factor antibodies), veganism, malabsorption. "
            "Neurological features: subacute combined degeneration of spinal cord (posterior columns + lateral corticospinal tracts), peripheral neuropathy. "
            "Treatment: IM hydroxocobalamin 1mg alternate days for 2 weeks then every 3 months; oral B12 high-dose for dietary deficiency. "
            "Folate deficiency anemia: macrocytic without neurological features, causes poor diet, pregnancy (supplement all women — 5mg folic acid), alcohol, methotrexate, phenytoin. "
            "Anemia of chronic disease: normocytic normochromic, low serum iron, low TIBC, high ferritin — treat underlying disease. "
            "Hemolytic anemia: premature red cell destruction — check reticulocytes, LDH, bilirubin, haptoglobin, Coombs test (autoimmune). "
            "Sickle cell disease: HbS polymerization, vaso-occlusive crises (severe pain), acute chest syndrome, stroke, splenic sequestration."
        ),
    },

    # ══════════════════════ GENERAL HEALTH ══════════════════════

    {
        "title": "Common Medications — Uses and Side Effects",
        "category": "general",
        "text": (
            "Paracetamol (acetaminophen): analgesic and antipyretic, dose 500mg–1g every 4–6 hours, maximum 4g/day. "
            "Safe in pregnancy. Overdose causes liver failure — treat with N-acetylcysteine. Avoid in severe liver disease. "
            "Ibuprofen (NSAID): anti-inflammatory, analgesic, antipyretic, dose 400–600mg TID. "
            "Side effects: GI irritation (take with food), peptic ulcer (use PPI if high risk), renal impairment, fluid retention, hypertension, "
            "cardiovascular risk (avoid in heart disease, CKD). Avoid in pregnancy (third trimester). "
            "Amoxicillin: broad-spectrum penicillin antibiotic, dose 250–500mg TID for respiratory, skin, ear infections. "
            "Side effects: diarrhea, nausea, rash. Contraindicated in penicillin allergy. "
            "Metformin: biguanide for type 2 diabetes, dose 500mg BD increasing to 1g BD. "
            "Side effects: GI (diarrhea, nausea, metallic taste — take with food), lactic acidosis (rare, hold for contrast dye/surgery). "
            "Contraindicated: eGFR <30, acute illness. Does not cause hypoglycemia. "
            "Amlodipine: calcium channel blocker for hypertension and angina, dose 5–10mg once daily. "
            "Side effects: peripheral edema (ankle swelling), flushing, headache, palpitations. Safe in CKD. "
            "Omeprazole/lansoprazole (PPIs): for GERD, peptic ulcer, H. pylori eradication, dose 20–40mg before breakfast. "
            "Side effects: headache, diarrhea, long-term — hypomagnesemia, C. diff risk, possible B12 deficiency, hip fractures. "
            "Atorvastatin: statin for dyslipidemia and cardiovascular prevention, dose 10–80mg at night. "
            "Side effects: myalgia, rarely rhabdomyolysis (check CK if muscle pain), elevated transaminases. "
            "Interactions: avoid with azithromycin, clarithromycin. "
            "Aspirin: low-dose 75–100mg for antiplatelet therapy in cardiovascular disease. "
            "Higher doses for pain/inflammation. Side effects: GI bleeding (use PPI), avoid in children under 16. "
            "Warfarin: anticoagulant for AF, DVT, PE, prosthetic valves. "
            "INR monitoring required (target 2–3 for most indications). "
            "Drug and food interactions extensive (vitamin K, antibiotics, NSAIDs). Antidote: vitamin K, FFP, PCC. "
            "Salbutamol (albuterol): SABA bronchodilator for asthma/COPD, inhaled 100–200mcg as needed. "
            "Side effects: tremor, tachycardia, hypokalemia with high doses."
        ),
    },

    {
        "title": "Preventive Medicine and Vaccinations",
        "category": "general",
        "text": (
            "Preventive medicine aims to protect, promote, and maintain health and reduce disease burden. "
            "Screening — detecting disease before symptoms: cervical smear (HPV testing + cytology every 5 years, women 25–65), "
            "mammography (breast cancer, women 50–70 every 3 years), colonoscopy (colorectal cancer, age 50–75 every 10 years or stool FIT test annually), "
            "PSA test (prostate cancer — controversial, shared decision making), lung CT (smokers age 50–80), "
            "BP measurement (all adults), cholesterol (men >40, women >50 or with risk factors), diabetes screening (HbA1c or fasting glucose). "
            "Vaccinations — UK NHS schedule: at birth — BCG (high-risk areas), Hepatitis B. "
            "8 weeks: 6-in-1 (diphtheria, tetanus, pertussis, polio, Hib, Hep B), meningococcal B, rotavirus. "
            "12 weeks: 6-in-1 (second dose), PCV13, rotavirus (second dose). "
            "16 weeks: 6-in-1 (third dose), meningococcal B (second dose). "
            "1 year: Hib/MenC, PCV13 booster, MMR, meningococcal B (third dose). "
            "3–4 years: 4-in-1 (DTaP/IPV), MMR (second dose). "
            "11–14 years: HPV (girls and boys, 2 doses), Td/IPV. "
            "Adults: annual flu vaccine (all >50, chronic conditions, pregnant, healthcare workers), "
            "COVID-19 booster, pneumococcal (PPSV23 for ≥65 and high risk), shingles (Shingrix, ≥70 years), "
            "hepatitis B (healthcare workers, high risk), meningococcal ACWY (university students, asplenia), "
            "travel vaccines (typhoid, hepatitis A, yellow fever, rabies, Japanese encephalitis, ETEC). "
            "Chemoprophylaxis: aspirin for high cardiovascular risk, statins for high cholesterol, PrEP for HIV prevention, "
            "antimalarials for travel, isoniazid for latent TB."
        ),
    },

    {
        "title": "Nutrition and Healthy Lifestyle",
        "category": "general",
        "text": (
            "Good nutrition and lifestyle are the foundation of health and disease prevention. "
            "Healthy diet: Mediterranean diet (olive oil, fish, vegetables, legumes, whole grains, nuts, moderate red wine) reduces cardiovascular disease, diabetes, cancer risk. "
            "DASH diet (Dietary Approaches to Stop Hypertension): low sodium, high potassium, magnesium, calcium — reduces BP by 8–14 mmHg. "
            "Macronutrients: carbohydrates 45–65% calories (whole grains, legumes), proteins 10–35% (lean meat, fish, legumes, dairy), fats 20–35% (unsaturated preferred). "
            "Micronutrients of concern: iron (meat, legumes, fortified cereals), calcium (dairy, leafy greens, fortified foods), vitamin D (sunlight, oily fish, supplements), "
            "B12 (animal products — vegans must supplement), folate (green vegetables, legumes, fortified foods), iodine (dairy, seafood, iodized salt). "
            "Water: 2–3 liters daily (more in heat and exercise). "
            "Physical activity guidelines: 150–300 minutes moderate aerobic activity per week (brisk walking, cycling, swimming) "
            "or 75–150 minutes vigorous activity (running, HIIT), plus muscle-strengthening 2+ days/week, reduce sedentary time. "
            "Exercise benefits: reduces cardiovascular disease 35%, diabetes 40–50%, depression, all-cause mortality; improves bone density, mental health, sleep, cognition. "
            "Smoking: causes 7 million deaths annually, major risk for lung cancer, COPD, cardiovascular disease, stroke, diabetes. "
            "Cessation: NRT (patches, gum, inhalers), varenicline (most effective), bupropion. "
            "Alcohol: maximum 14 units/week for men and women (UK), no more than 3–4 days. "
            "Excess alcohol causes liver disease (fatty liver → hepatitis → cirrhosis), cancer, cardiovascular disease, pancreatitis, neuropathy. "
            "Sleep: 7–9 hours per night for adults; chronic sleep deprivation increases obesity, diabetes, cardiovascular disease, depression, dementia risk. "
            "BMI: normal 18.5–24.9, overweight 25–29.9, obese ≥30. Even 5–10% weight loss significantly improves metabolic health."
        ),
    },

    {
        "title": "Pain Management — Analgesic Ladder",
        "category": "general",
        "text": (
            "Pain is the most common reason people seek medical care. Assessment is crucial: SOCRATES (Site, Onset, Character, Radiation, Associations, Time course, Exacerbating/relieving factors, Severity). "
            "WHO analgesic ladder (originally for cancer pain, now used broadly): "
            "Step 1 (mild pain): non-opioid analgesics — paracetamol 1g QDS, NSAIDs (ibuprofen 400mg TID, naproxen 500mg BD, diclofenac 50mg TID), "
            "topical NSAIDs/capsaicin for localized musculoskeletal pain. "
            "Step 2 (moderate pain): weak opioids — codeine 30–60mg QDS (often combined with paracetamol as co-codamol), tramadol 50–100mg QDS (serotonin syndrome risk), dihydrocodeine. "
            "Step 3 (severe pain): strong opioids — morphine (oral immediate-release 5–10mg every 4 hours), oxycodone, hydromorphone, "
            "fentanyl patches (for stable chronic pain — 72-hour patches). "
            "Adjuvant analgesics: anticonvulsants (gabapentin 300–3600mg/day, pregabalin 75–600mg/day — neuropathic pain), "
            "TCAs (amitriptyline 10–75mg at night — neuropathic, migraine prevention), SNRIs (duloxetine — diabetic neuropathy, fibromyalgia), "
            "muscle relaxants (diazepam, baclofen — muscle spasm), ketamine (procedural/cancer pain), lidocaine patches. "
            "Opioid side effects: constipation (always prescribe laxatives), nausea, sedation, respiratory depression (naloxone reversal), dependence, tolerance. "
            "Avoid opioids for chronic non-cancer pain where possible — physiotherapy, CBT, multidisciplinary pain management preferable. "
            "Neuropathic pain first-line: duloxetine, pregabalin or gabapentin, amitriptyline. "
            "Migraine: triptans (sumatriptan 50–100mg) + NSAID/aspirin for acute; topiramate, propranolol, amitriptyline for prevention."
        ),
    },

    {
        "title": "COVID-19 Long COVID and Post-Viral Syndromes",
        "category": "infections",
        "text": (
            "Long COVID (post-acute sequelae of SARS-CoV-2 infection, PASC) affects an estimated 10–30% of COVID-19 survivors. "
            "Defined as symptoms persisting or developing more than 4 weeks after acute infection. "
            "Most common symptoms: fatigue (most common — 58%), post-exertional malaise (worsening after physical or mental activity), "
            "breathlessness, cognitive impairment ('brain fog' — concentration, memory, word-finding difficulties), "
            "palpitations, chest pain or tightness, headache, sleep disturbance, depression and anxiety, joint and muscle pain, "
            "persistent cough, smell and taste disturbances (parosmia — distorted smell), hair loss, skin rashes. "
            "Cardiovascular: myocarditis, pericarditis, postural orthostatic tachycardia syndrome (POTS — tachycardia on standing, dizziness, fatigue). "
            "Pathophysiology: viral persistence, immune dysregulation, autoantibodies, microclots (microthrombi), mitochondrial dysfunction, reactivation of EBV/herpes viruses. "
            "Diagnosis is clinical — exclude other conditions. Investigations: ECG, echocardiogram, pulmonary function tests, brain MRI, immunological testing. "
            "Management: multidisciplinary approach — general practitioners, physiotherapists, occupational therapists, psychologists, specialist services. "
            "Activity pacing (avoid boom-bust cycle), gradual rehabilitation for those without post-exertional malaise, heart rate monitoring. "
            "Specific treatments: POTS — increased salt/fluid intake, compression garments, propranolol, ivabradine, fludrocortisone. "
            "Breathlessness — breathing retraining, pulmonary rehabilitation. "
            "Cognitive rehabilitation — structured programs. Low-dose naltrexone, antihistamines (for mast cell activation) — some benefit in research. "
            "Vaccination reduces long COVID risk by 50%. No definitive cure yet — active research ongoing."
        ),
    },

    {
        "title": "Skin Conditions — Eczema, Psoriasis, Acne",
        "category": "dermatology",
        "text": (
            "Atopic dermatitis (eczema): chronic inflammatory skin condition with intense itch, dry skin, and recurrent flares. "
            "Common in children (affects 20%), persists into adulthood in 30%. Associated with asthma and allergic rhinitis (atopic triad). "
            "Triggers: soaps, detergents, dust mites, pet dander, stress, sweating, infections, certain foods in children. "
            "Treatment: emollients (moisturizers) applied liberally and frequently (most important — aqueous cream, E45, Doublebase), "
            "topical corticosteroids (mild — 1% hydrocortisone for face/flexures; moderate — clobetasone butyrate; potent — betamethasone valerate; very potent — clobetasol), "
            "topical calcineurin inhibitors (tacrolimus, pimecrolimus — steroid-sparing, face and folds), "
            "antihistamines for itch (chlorphenamine for sleep), antibiotics for infected eczema (flucloxacillin for Staph aureus), "
            "dupilumab (IL-4/13 inhibitor biologic — severe refractory adult eczema), phototherapy (NB-UVB). "
            "Psoriasis: chronic autoimmune condition — rapid skin cell turnover causing thick, scaly plaques (salmon-pink with silver scale), "
            "affecting scalp, elbows, knees, lower back, nails (pitting, onycholysis). Affects 2–3% population. "
            "Psoriatic arthritis in 20–30%. "
            "Treatment: topical (vitamin D analogues — calcipotriol, corticosteroids, coal tar), "
            "phototherapy (PUVA, NB-UVB), systemic (methotrexate, ciclosporin, acitretin), biologics (TNF inhibitors, IL-17 inhibitors — secukinumab, ixekizumab, IL-23 inhibitors — ustekinumab, risankizumab). "
            "Acne vulgaris: comedones (blackheads/whiteheads), papules, pustules, nodules, cysts from follicular obstruction and Cutibacterium acnes infection. "
            "Mild: topical benzoyl peroxide, retinoids (tretinoin, adapalene), topical antibiotics (clindamycin). "
            "Moderate: oral antibiotics (doxycycline 100mg BD for 3 months), combined with topical. "
            "Severe/nodular: oral isotretinoin (0.5–1 mg/kg/day — highly teratogenic, need REMS program, monthly pregnancy tests)."
        ),
    },

    {
        "title": "Eye Diseases — Common Conditions",
        "category": "ophthalmology",
        "text": (
            "Glaucoma: optic nerve damage from raised intraocular pressure (IOP), progressive visual field loss. "
            "Primary open-angle glaucoma (most common): painless, insidious, peripheral vision loss first — often silent until advanced. "
            "Acute angle-closure glaucoma: emergency — sudden severe eye pain, red eye, fixed mid-dilated pupil, nausea, vomiting, headache, haloes around lights. "
            "Treatment: eye drops — prostaglandin analogues (latanoprost, bimatoprost — first-line, once daily), beta-blockers (timolol), "
            "carbonic anhydrase inhibitors (dorzolamide), alpha-2 agonists (brimonidine). Laser trabeculoplasty, surgical trabeculectomy. "
            "Cataract: clouding of lens — gradual blurred vision, glare, difficulty with bright lights, colors appear faded. "
            "Risk: age, UV exposure, diabetes, steroids, trauma. Treatment: phacoemulsification surgery with intraocular lens implant — highly effective. "
            "Age-related macular degeneration (AMD): central vision loss in elderly. "
            "Dry AMD (80%): drusen deposits, slow progression, no cure — supplements (AREDS2 — lutein, zeaxanthin, zinc, vitamins C/E) slow progression. "
            "Wet AMD (20%): neovascularization — rapid central vision loss, metamorphopsia (distortion). "
            "Treatment: anti-VEGF injections (ranibizumab, aflibercept, bevacizumab) given monthly/bimonthly — preserves or improves vision. "
            "Diabetic retinopathy: most common cause of blindness in working-age adults. Non-proliferative to proliferative (new vessel formation). "
            "Prevention: tight glucose and BP control. Treatment: laser photocoagulation, anti-VEGF injections, vitrectomy. "
            "Conjunctivitis: red eye, discharge. Bacterial (purulent) — chloramphenicol drops. "
            "Viral (adenovirus — watery discharge) — self-limiting. Allergic — antihistamine drops, avoid allergens."
        ),
    },

]

