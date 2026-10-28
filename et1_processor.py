import os

# Define our directory tracking lines
SOURCE_FILE = "raw_data.csv"
TARGET_FILE = "clean_archive.txt"

def run_etl():
    # 1. Check if a new file has dropped into the landing zone
    if not os.path.exists(SOURCE_FILE):
        print(" Pipeline Idle: No raw_data.csv file found to process.")
        return

    print(" File Detected! Running ETL Pipeline...")

    # 2. Extract & Transform
    try:
        with open(SOURCE_FILE, "r") as src, open(TARGET_FILE, "a") as dest:
            # Skip the header row
            header = src.readline()
            
            for line in src:
                # Split row items by comma
                row = line.strip().split(",")
                if len(row) < 3: continue
                
                txn_id, amount, status = row[0], row[1], row[2]
                
                # Business Rule Filter: Only archive completed sales
                if status.lower() == "completed":
                    dest.write(f"TXN_LOG -> ID: {txn_id} | Cleaned Amount: INR {amount}\n")
        
        # 3. Clean Up: Delete the raw source file so we don't process it twice
        os.remove(SOURCE_FILE)
        print(" Success: Processing complete. Raw landing file cleared.")

    except Exception as e:
        print(f" Pipeline crashed: {e}")

if __name__ == "__main__":
    run_etl()
