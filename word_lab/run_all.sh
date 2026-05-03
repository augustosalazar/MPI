#!/bin/sh

set -eu

APP_DIR="/app"
RESULTS_DIR="$APP_DIR/results"
LOG_DIR="$RESULTS_DIR/logs"
SUMMARY_FILE="$RESULTS_DIR/times_summary.csv"
NP_LIST="${NP_LIST:-2 4 8}"
RUNS="${RUNS:-3}"

if [ -d "$RESULTS_DIR" ]; then
  echo "Removing existing results directory: $RESULTS_DIR"
  rm -rf "$RESULTS_DIR"
fi

mkdir -p "$RESULTS_DIR"
mkdir -p "$LOG_DIR"

echo "program,np,run,time_seconds" > "$SUMMARY_FILE"

extract_time() {
  grep "EXECUTION_TIME=" "$1" | tail -n 1 | cut -d= -f2
}

echo "======================================"
echo "1) Generating dataset"
echo "======================================"
python "$APP_DIR/generator.py" | tee "$LOG_DIR/generator.log"

echo ""
echo "======================================"
echo "2) Running sequential baseline"
echo "======================================"
BASELINE_LOG="$LOG_DIR/baseline_secuencial.log"
python "$APP_DIR/baseline_secuencial.py" | tee "$BASELINE_LOG"

BASELINE_TIME=$(extract_time "$BASELINE_LOG" || true)
if [ -n "${BASELINE_TIME:-}" ]; then
  echo "baseline,1,1,$BASELINE_TIME" >> "$SUMMARY_FILE"
fi

echo ""
echo "======================================"
echo "3) Running MPI version 1"
echo "======================================"

for NP in $NP_LIST
do
  for RUN in $(seq 1 "$RUNS")
  do
    LOG_FILE="$LOG_DIR/mpi1_np${NP}_run${RUN}.log"
    echo ""
    echo "Running mpi1.py with np=$NP, run=$RUN"
    mpirun --allow-run-as-root --oversubscribe -np "$NP" python "$APP_DIR/mpi1.py" | tee "$LOG_FILE"

    RUN_TIME=$(extract_time "$LOG_FILE" || true)
    if [ -n "${RUN_TIME:-}" ]; then
      echo "mpi1,$NP,$RUN,$RUN_TIME" >> "$SUMMARY_FILE"
    fi
  done
done

echo ""
echo "======================================"
echo "4) Running MPI version 2"
echo "======================================"

for NP in $NP_LIST
do
  for RUN in $(seq 1 "$RUNS")
  do
    LOG_FILE="$LOG_DIR/mpi2_np${NP}_run${RUN}.log"
    echo ""
    echo "Running mpi2.py with np=$NP, run=$RUN"
    mpirun --allow-run-as-root --oversubscribe -np "$NP" python "$APP_DIR/mpi2.py" | tee "$LOG_FILE"

    RUN_TIME=$(extract_time "$LOG_FILE" || true)
    if [ -n "${RUN_TIME:-}" ]; then
      echo "mpi2,$NP,$RUN,$RUN_TIME" >> "$SUMMARY_FILE"
    fi
  done
done

echo ""
echo "======================================"
echo "Done"
echo "======================================"
echo "Logs available in: $LOG_DIR"
echo "Summary CSV: $SUMMARY_FILE"
