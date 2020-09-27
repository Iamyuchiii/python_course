#!/usr/bin/env nextflow

/*
 * Setting the params for the pipeline
 * The pipeline is designed for paired-end reads
 */

params.reads = "$baseDir/bin/input_data/*R{1,2}.fasls
tq.gz"
//params.bowtie2_index = "$baseDir/bin/databases/bowtie2_human_index/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.bowtie_index"
//params.bowtie2_index_full_ana = "$baseDir/bin/databases/bowtie2_human_index_full_ana/GCA_000001405.15_GRCh38_full_analysis_set.fna.bowtie_index"
params.outDir = "$baseDir/pipeline_test/"


reads = "$params.reads"
//bowtie2_index = "$params.bowtie2_index"
//bowtie2_index_full = "$params.bowtie2_index_full_ana"
outDir = "$params.outDir"


"""
============
=  fastp  =
============
"""
params.min_reads_length = 80

min_reads_length = "$params.min_reads_length"

"""
=================
=  Subsampling  =
=================
"""
params.seqtk_seeds = 100
params.seqtk_percentage = 0.1

seqtk_seeds = "$params.seqtk_seeds"
seqtk_percentage = "$params.seqtk_percentage"

"""
=======================
=  Cores and threads  =
=======================
"""
params.threads = 6
params.cores = 3

threads = "$params.threads"
cores = "$params.cores"
"""
======================
=  Pipeline setting  =
======================
"""
params.assembly_mode = "metaspades"
//params.reads_filter = true
params.subsampling_run = false
params.assembly = true

assembly_mode = "$params.assembly_mode"
//reads_filter = "$params.reads_filter"
assembly = "$params.assembly"


/*
Creating input channels for fastqc and fastp
Input file: $params.reads
Channel created: channel_fastqc, channel_fastp
*/
Channel
        .fromFilePairs(params.reads) //reads the files as a pair
        .ifEmpty{"Please put the paired reads in input_map"} // check if the reads are being loaded into the channel
        .into{ channel_fastqc; channel_fastp } // putting the reads into channels


/*
Running fastqc with default option
input: params.reads
Channel created: channel_fastqc
 */
process fastqc {
    publishDir "${outDir}${sampleID}/fastqc/before_trim", mode: "copy"
    input:
    set sampleID, file(reads) from channel_fastqc
    output:
    set sampleID, file("*") into channel_multiqc_fastqc_before
    script:
    """
    fastqc -t ${cores} ${reads[0]} ${reads[1]}
    """
}

/*
input: params.reads
output: trimmed reads in pair
Channel used: channel_fastp
Channel created: channel_trimmed_fastqc, channel_classification, channel_host_read_remove, channel_subsampling
 */
process fastp {
    publishDir "${outDir}${sampleID}/fastp", mode: "copy"
    input:
    set sampleID, file(reads) from channel_fastp
    output:
    set sampleID, file("${sampleID}_R1_trim.fastq.gz"), file("${sampleID}_R2_trim.fastq.gz") into channel_trimmed_fastqc, channel_classification, channel_host_read_remove, channel_subsampling
    file("${sampleID}_R1_2_trim_fastp.json") into channel_multiqc_fastp
    file("*")
    script:
    """
    fastp -i ${reads[0]} -I ${reads[1]} -w ${threads} -l ${min_reads_length} \
    -o ${sampleID}_R1_trim.fastq.gz -O ${sampleID}_R2_trim.fastq.gz \
    -j ${sampleID}_R1_2_trim_fastp.json -h ${sampleID}_R1_2_trim_fastp.html
    """
}

/*
input: trimmed reads in pair from fastp
Channel used: channel_trimmed_fastqc
Channel created: channel_multiqc_fastqc_after
 */
process fastqc_after_trimming {
    publishDir "${outDir}${sampleID}/fastqc/after_trim", mode: "copy"
    input:
    set sampleID, file("${sampleID}_R1_trim.fastq.gz"), file("${sampleID}_R2_trim.fastq.gz") from channel_trimmed_fastqc
    output:
    file("*") into channel_multiqc_fastqc_after
    """
    fastqc -t ${cores} ${sampleID}_R1_trim.fastq.gz ${sampleID}_R2_trim.fastq.gz
    """
}




"""
======================================
= Classification with host filtering =
======================================
"""
/*
input: trimmed reads in pair from fastp
Channel used: channel_subsampling
Channel created: None
 */
/*
process host_background_remove {
    publishDir "${outDir}${sampleID}/host_reads_removed", mode: "copy"
    input:
    set sampleID, file("${sampleID}_R1_trimmed.fastq.gz"), file("${sampleID}_R2_trimmed.fastq.gz") from channel_host_read_remove
    output:
    file("*") into channel_multiqc_bowtie2
    set sampleID, file("${sampleID}_R1_host_removed.fastq.gz"), file("${sampleID}_R2_host_removed.fastq.gz") into channel_fastqc_host_removed, channel_classification_host_removed, channel_assembly
    when:
    reads_filter == true && subsampling_run == false
    script:
    """
    # bowtie2 maps the reads against the database
    bowtie2 -p ${cores} -x ${bowtie2_index} -1 ${sampleID}_R1_trimmed.fastq.gz -2 ${sampleID}_R2_trimmed.fastq.gz -S ${sampleID}1_2_mapped_ummapped.sam
    # samtools converts sam file to bam file
    samtools view -@ ${threads} -bS ${sampleID}1_2_mapped_ummapped.sam > ${sampleID}1_2_mapped_ummapped.bam
    # samtools removes all reads that are mapped against the database
    samtools view -@ ${threads} -b -f 12 ${sampleID}1_2_mapped_ummapped.bam > ${sampleID}1_2_bothEndsUnmapped.bam
    # samtools sorts the reads for seperation
    samtools sort -@ ${threads} -n -o ${sampleID}1_2_sorted_all.bam ${sampleID}1_2_bothEndsUnmapped.bam
    # bedtools seperates the reads in pair from the bam file
    bedtools bamtofastq -i ${sampleID}1_2_sorted_all.bam -fq ${sampleID}_R1_host_removed.fastq -fq2 ${sampleID}_R2_host_removed.fastq
    gzip ${sampleID}_R1_host_removed.fastq
    gzip ${sampleID}_R2_host_removed.fastq
    """
}

/*
Running fastqc with default option (threads 6)
input: trimmed reads in pair from fastp
*/
process fastqc_after_host_removed {
    publishDir "${outDir}${sampleID}/host_reads_removed/fastqc", mode: "copy"
    input:
    set sampleID, file("${sampleID}_R1_host_removed.fastq.gz"), file("${sampleID}_R2_host_removed.fastq.gz") from channel_fastqc_host_removed
    output:
    path("*") into channel_multiqc_after_host_remove
    """
    fastqc -t ${cores} ${sampleID}_R1_host_removed.fastq.gz ${sampleID}_R2_host_removed.fastq.gz
    """
}
*/

"""
============
= Assembly =
============
"""

process assembly {
    publishDir "${outDir}${sampleID}/assembly", mode: "copy"
    input:
    set sampleID, file("${sampleID}_R1_host_removed.fastq.gz"), file("${sampleID}_R2_host_removed.fastq.gz") from channel_assembly
    output:
    file ("*")
    file ("contigs.fasta") optional true into channel_metaspades
    file ("final.contigs.fa") optional true into channel_megahit
    when:
    assembly == true
    script:
    if (assembly_mode == "metaspades")
    """
    metaspades.py -t ${threads} -1 ${sampleID}_R1_host_removed.fastq.gz -2 ${sampleID}_R2_host_removed.fastq.gz -o metaspades
    """
}
