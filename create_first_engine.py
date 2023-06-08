from sqlalchemy import create_engine #We need to import some utils to be able to create an engine

engine_alexandria = create_engine(f'sqlite:///db/Alexandria.db') #We create an engine by specifying the path of our DB file
