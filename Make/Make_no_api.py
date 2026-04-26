print('Installing Libraries')

import subprocess
import papermill as pm

subprocess.check_call(['pip', 'install','papermill','requests', 'pandas','beautifulsoup4','sentence-transformers','python-dateutil', 'newsapi-python','python-dotenv', 'yfinance','transformers', 'torch','statsmodels', 'matplotlib', 'scikit-learn', 'scipy',
    'huggingface_hub', 'folium','jupyter'])

print('Libraries all installed')
print('Running Sentiment and Outputs, will update after each script complete, this may take a couple of minutes (see README)')

pm.execute_notebook('Scripts/Sentiment.ipynb', output_path='Scripts/Sentiment.ipynb', cwd='.')

print ('Sentiment complete')

pm.execute_notebook('Scripts/Outputs.ipynb', output_path='Scripts/Outputs.ipynb', cwd='.')

print('outputs complete')

print('All scripts executed')
