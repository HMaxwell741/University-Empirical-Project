print('Installing Libraries')

import subprocess
import papermill as pm

subprocess.check_call(['pip', 'install','papermill','requests', 'pandas','beautifulsoup4','sentence-transformers','python-dateutil', 'newsapi-python','python-dotenv', 'yfinance','transformers', 'torch','statsmodels', 'matplotlib', 'scikit-learn', 'scipy',
    'huggingface_hub', 'folium','jupyter'])

print('Libraries all installed')
print('Running Scripts, will update after each script complete, this may take a couple of minutes (see README)')

pm.execute_notebook('Scripts/Scraping.ipynb', output_path='Scripts/Scraping.ipynb', cwd='Scripts')

print('Scraping complete')

pm.execute_notebook('Scripts/Sentiment.ipynb', output_path='Scripts/Sentiment.ipynb', cwd='Scripts')

print ('Sentiment complete')

pm.execute_notebook('Scripts/Outputs.ipynb', output_path='Scripts/Outputs.ipynb', cwd='Scripts')

print('outputs complete')

print('All scripts executed')
