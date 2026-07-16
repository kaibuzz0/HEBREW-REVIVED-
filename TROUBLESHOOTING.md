# Troubleshooting

## Common Issues

### "Database not found"
**Solution:** Database is in `data/complete_bible.db`

### "Python not found" (Windows)
**Solution:** 
1. Install Python from https://python.org
2. Check "Add Python to PATH" during installation
3. Restart terminal

### "Permission denied" (Linux/macOS)
**Solution:**
```bash
chmod +x launch.py
python3 launch.py
```

### Slow searches
**Solution:** Run `python3 update.py` to optimize database

### Out of memory
**Solution:** 
- Close other applications
- Use `export_csv.py` for smaller chunks

## Getting Help

1. Run `python3 validate.py` to check system
2. Check `QUICKSTART.md` for basics
3. See `README.md` for full docs
4. Check GitHub issues

## Reset Everything

```bash
# Backup first
python3 backup.py

# Reset (keeps database)
rm -rf __pycache__
python3 validate.py
```
