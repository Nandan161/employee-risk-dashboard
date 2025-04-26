def report(id, entity):
    try:
        print(f"Generating report for ID: {id}, Entity: {entity}")

        # Example logic — replace with your actual content
        username = entity.username(id)
        model_df = entity.model_data(id)
        notes_df = entity.notes(id)
        events_df = entity.event_counts(id)

        print("Fetched data successfully")

        return {
            "username": username,
            "model_data": model_df.to_dict(),
            "notes": notes_df.to_dict(orient="records"),
            "events": events_df.to_dict(orient="records")
        }

    except Exception as e:
        print(f"Error in report(): {e}")
        return {"error": "Something went wrong with the report generation."}
